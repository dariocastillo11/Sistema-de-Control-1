import numpy as np

# Parámetros LoRa
SF = 7
N = 2 ** SF
n_symbols = 8
preamble_len = 8

# 1. Generación de símbolos aleatorios (datos)
data_symbols = np.random.randint(0, N, n_symbols)

# 2. Construcción de la trama (preambulo + datos)
frame = np.concatenate([np.zeros(preamble_len, dtype=int), data_symbols])

# 3. Modulación LoRa (Chirp Spread Spectrum)
def lora_modulate(symbols, SF):
    N = 2 ** SF
    k = np.arange(N)
    signal = []
    for s in symbols:
        phase = 2 * np.pi * ((s * k / N) + (k**2) / (2*N))
        chirp = np.exp(1j * phase)
        signal.append(chirp)
    return np.concatenate(signal)

tx_signal = lora_modulate(frame, SF)

# --- Canal (puedes agregar ruido aquí si quieres) ---
# rx_signal = tx_signal + ruido
rx_signal = tx_signal  # Ideal

# 4. Receptor LoRa con etapas extra

def window_alignment(rx_signal, SF, preamble_len):
    N = 2 ** SF
    search_range = N  # Buscar dentro de un símbolo
    max_energy = 0
    best_offset = 0
    k = np.arange(N)
    base_chirp = np.exp(1j * 2 * np.pi * (k**2) / (2*N))
    # Buscar la mejor alineación usando el preámbulo
    for offset in range(search_range):
        energies = []
        for i in range(preamble_len):
            idx = offset + i*N
            if idx+N > len(rx_signal):
                break
            r = rx_signal[idx:idx+N]
            dechirped = r * np.conj(base_chirp)
            spectrum = np.fft.fft(dechirped)
            energies.append(np.max(np.abs(spectrum)))
        total_energy = np.sum(energies)
        if total_energy > max_energy:
            max_energy = total_energy
            best_offset = offset
    return best_offset

def peak_merging(spectrum, threshold=0.5):
    # Si hay varios picos cercanos, fusionar (aquí solo devuelve el mayor)
    abs_spec = np.abs(spectrum)
    max_val = np.max(abs_spec)
    peaks = np.where(abs_spec > threshold * max_val)[0]
    # Si hay varios picos, devolver el promedio (mod N)
    if len(peaks) > 1:
        return int(np.round(np.mean(peaks))) % len(spectrum)
    else:
        return peaks[0]

def lora_demodulate(rx_signal, SF, preamble_len):
    N = 2 ** SF
    # --- Window Alignment ---
    offset = window_alignment(rx_signal, SF, preamble_len)
    rx_signal = rx_signal[offset:]
    n_symbols = len(rx_signal) // N
    rx_signal = rx_signal[:n_symbols * N].reshape((n_symbols, N))
    k = np.arange(N)
    base_chirp = np.exp(1j * 2 * np.pi * (k**2) / (2*N))
    symbols_rx = []
    for r in rx_signal:
        dechirped = r * np.conj(base_chirp)
        spectrum = np.fft.fft(dechirped)
        # --- Peak Merging ---
        symbol_hat = peak_merging(spectrum)
        symbols_rx.append(symbol_hat)
    # --- Clock Recovery ---
    # En simulación ideal, no es necesario. En SDR, aquí ajustarías el muestreo.
    return np.array(symbols_rx[preamble_len:])

symbols_rx = lora_demodulate(rx_signal, SF, preamble_len)

print("Símbolos transmitidos:", data_symbols)
print("Símbolos detectados:  ", symbols_rx)
print("SER:", np.mean(data_symbols != symbols_rx))

import matplotlib.pyplot as plt
# Visualizar la magnitud de la señal transmitida (primeros 2 símbolos)
plt.figure(figsize=(10,3))
plt.plot(np.abs(tx_signal[:2*N]))
plt.title('Magnitud de la señal LoRa (2 símbolos)')
plt.xlabel('Muestra')
plt.ylabel('Magnitud')

# Calcular el espectro de un símbolo dechirpeado (por ejemplo, el primero de datos)
k = np.arange(N)
base_chirp = np.exp(1j * 2 * np.pi * (k**2) / (2*N))
offset = window_alignment(rx_signal, SF, preamble_len)
r = rx_signal[offset:][:N]
dechirped = r * np.conj(base_chirp)
spectrum = np.fft.fft(dechirped)

plt.figure()
plt.plot(np.abs(spectrum))
plt.title('FFT de un símbolo dechirpeado')
plt.xlabel('Índice FFT')
plt.ylabel('Magnitud')

# Calcular energía de dechirping para cada offset (Window Alignment)
energies = []
for off in range(N):
    total = 0
    for i in range(preamble_len):
        idx = off + i*N
        if idx+N > len(rx_signal):
            break
        r = rx_signal[idx:idx+N]
        dechirped = r * np.conj(base_chirp)
        spectrum_tmp = np.fft.fft(dechirped)
        total += np.max(np.abs(spectrum_tmp))
    energies.append(total)

plt.figure()
plt.plot(energies)
plt.title('Energía de dechirping vs offset (Window Alignment)')
plt.xlabel('Offset')
plt.ylabel('Energía total')

plt.show()