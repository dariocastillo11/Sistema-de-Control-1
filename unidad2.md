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
