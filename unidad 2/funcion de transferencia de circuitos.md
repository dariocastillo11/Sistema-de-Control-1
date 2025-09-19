# 📘 Unidad N° 2: *Representacion matematicas y grafica de sistemas lineales en tiempo continuo*
# 📝 2) Funciones de Transferencia de Circuitos Básicos
## 1. Determinar la función de transferencia que relaciona la tensión de salida con la tensión de entrada de los siguientes circuitos. Comparar los resultados.

### Circuito N° 1:
![](../imagen/circuito1.png)
```octave
close all; clear all; clc
syms R1 R2 C1 C2 s

# CIRCUITO 1:
# v(s) = i(s) * (r +(1/ (s*c)))
# i(s) = v(s) / (r +(1/ (s*c)))

# v_o(s) =        i(s) * (1/ (s*c)))
# v_i(s) = v(s) = i(s) * (r +(1/ (s*c)))
#                  ------------------
# v_o(s)/v_i(s) = (1/(s*c))) / (r +(1/(s*c)))

FT_1 = 1 / (s*C1*R1 + 1)
##########################
# CIRCUITO 2:
syms Vin I1 I2 Vout real
X1 = 1 / (s*C1);
X2 = 1 / (s*C2);
ec_1 = Vin == I1*(R1+X1) - I2*X1;
ec_2 = 0 == (-I1)*X1 + I2*(R2+X2+X1);
# DESPEJO I1 de ec_2
I1 = ((I2*(R2+X2+X1)) / X1) ;
#ec_3 = Vin == I1*(R1+X1) - I2*X1
ec_3 = Vin == ((I2*(R2+X2+X1)) / X1)*(R1+X1) - I2*X1;
# vout = I2 * X2
I2 = (Vout/X2);
#remplazo I2 EN E_4
#ec_4 = Vin == ((I2*(R2+X2+X1)) / X1)*(R1+X1) - I2*X1
ec_4 = Vin == (((Vout/X2)*(R2+X2+X1)) / X1)*(R1+X1) - (Vout/X2)*X1;
S = solve(ec_4,Vout);
G2 = S / Vin

disp("=== Termino el programa ===")
#########################
# CIRCUITO 3
# Esta compuesta por FT_1 CALCULADA ANTERIORMENTE
# Y una mas parecida: FT_2
FT_1 = 1 / (s*C1*R1 + 1) # LA YA CALCULADA
FT_2 = 1 / (s*C2*R2 + 1)
#Luego por propeidad de cascada
G3 = FT_1 * FT_2

```
## ⚙️ Resultados obtenidos
![](../imagen/g3.png)
#### En el circuito 2 cualquier modificaciond e valores de R Y C afecta a todos los polos. En cambio en el circuito 3 cualquier modificacion r1 c1 r2 c2 afecta a un solo polo. Esto se logra con el buffer para separar circuito
---
