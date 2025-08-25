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



