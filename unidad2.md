# 📘 Unidad N° 2: *Representacion matematicas y grafica de sistemas lineales en tiempo continuo*

# 📝 2) Algebra de bloques 
## Obtener la funcion de transferencia de los siguientes sistemas utilizando el algebra de bloques. Simular la respuesta al escalon.
---
### Sistema 1: sistema a lazo cerrado con realimentacion tacométrica

![](imagen/image.png)
## 💻 Código en Octave

```octave
# UNIDAD 2 . EJERCICIO NRO 2. sistema 1
close all; clear all; clc

s = tf('s');
#DEFINO LOS SISTEMAS:
kp = 31;
G1 = (53*(s+1)) / ((s+10)*(s+100));
kd = 16;
G2 = 1 / s;
#################

# USANDO MINREAL: SE USA PARA CANCELAR POLOS Y CEROS
disp("USANDO MINREAL")
FT_LC_1 = minreal(G1 / (1 + kd*G1))
FT_CASCADA = minreal(kp * G1 * G2)
FT_LC_TOTAL = minreal(FT_CASCADA/(1+FT_CASCADA))

disp("USANDO feedback")
#USNADO feedback: SE USA PARA SISTEMAS DE LAZO CERRADOS 
FT_LC_1 = feedback(G1,kd)
FT_CASCADA = minreal(kp * G1 * G2)
FT_LC_TOTAL = feedback(FT_CASCADA,1)

disp("termino el programa ")
```
## ⚙️ Resultados obtenidos
![](imagen/2.1.png)

---

### Sistema 2: sistema de control en cascada
![](imagen/2.3.png)
## 💻 Código en Octave

```octave
# UNIDAD 2 . EJERCICIO NRO 2. sistema 2
close all; clear all; clc
s = tf('s');
#DEFINO LOS SISTEMAS:
PI = (s+ 0.1) / s;
P = 12;
G1 = 27 / (s + 200);
G2 = 5 / (s + 0.1);
#################

FT_CASCADA1 = minreal(P * G1);
FT_LC_1 = minreal(FT_CASCADA1 / (1 + FT_CASCADA1))
FT_CASCADA_2 = minreal(FT_LC_1 * G2 * PI)
FT_LC_TOTAL = minreal(FT_CASCADA_2 / (1 + FT_CASCADA_2))

#usando feedback:2
FT_CASCADA1 = minreal(P * G1);
FT_LC_1 = feedback(FT_CASCADA1,1)
FT_CASCADA_2 = minreal(FT_LC_1 * G2 * PI)
FT_LC_TOTAL = feedback(FT_CASCADA_2,1)


disp("termino el programa ")


```
## ⚙️ Resultados obtenidos
![](imagen/sistema2.png)

---

### Sistema 3: sistema de lazo cerrado con controlador PID
![](imagen/SISTEMA3PREG.png)
## 💻 Código en Octave

```octave
# UNIDAD 2 . EJERCICIO NRO 2. sistema 3
close all; clear all; clc
pkg load symbolic
#defino las variables simbolicas
syms  kp ti td s wn p real
#DEFINO LOS SISTEMAS:
PLANTA_1 = (ti*td*s^2+ti*s+1) / (ti*s)
PLANTA_2 = (wn^2) / (s^2+2*p*wn*s+wn^2)
#################

FT_CASCADA_1 = simplify(kp*PLANTA_1*PLANTA_2)
FT_LC_TOTAL = simplify(FT_CASCADA_1 / (1 + FT_CASCADA_1))

#como son variables simbolicas no
#puedo usar minreal ni feedback 
#esas necesitan de valores 
```
## ⚙️ Resultados obtenidos
![](imagen/sistema3sol.png)
---

### Sistema 4: sistema de lazo cerrado con controlador PID
![](imagen/sistema4pregunta.png)
## 💻 Código en Octave

```octave
# UNIDAD 2 . EJERCICIO NRO 2. sistema 4
close all; clear all; clc
pkg load symbolic
syms ti td s kp t k 
#DEFINO LOS SISTEMAS:
GAIN_1 = 1/ti;
GAIN_2 = td;
GAIN_0 = kp;
G1 = k / (t*s+1);
FT_1 = 1/s;
FT_2 = s;
#################

FT_CASCADA_1 = GAIN_1*FT_1
FT_CASCADA_2 = GAIN_2*FT_2
FT_CASCADA_3 = GAIN_0*G1
ADD = simplify(1 + FT_CASCADA_1 + FT_CASCADA_2)
FT_CASCADA_TOTAL = simplify(ADD * FT_CASCADA_3)
FT_LC_1 = simplify(FT_CASCADA_TOTAL / (1+FT_CASCADA_TOTAL))

```
## ⚙️ Resultados obtenidos
![](imagen/sistema4sol.png)

# 📝 3) 
## En la figura se muestra el diagrama de bloques de un motor de corriente continua, donde E(s) representa la entrada de tensión, W(s) la salida de velocidad del eje,    I(s) la corriente que circula por el motor y T_L(S) la carga del sistema, que puede verse como una perturbación. Se pide: 
### 3.1. Determinar las cuatro funciones de transferencia que modelan el sistema.  
### 3.2. Simular la respuesta del sistema para e(t)=24*u(t)  y T_L(t)=0.01*u(t-2)
---
![](imagen/EJ3.png)
## 💻 Código en Octave
```octave

```
## ⚙️ Resultados obtenidos
![](imagen/)

---