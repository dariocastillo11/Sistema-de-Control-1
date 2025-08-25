# UNIDAD 2 . EJERCICIO NRO 2. sistema 2
close all; clear all; clc
s = tf('s');
#DEFINO LOS SISTEMAS:
PI = (s+ 0.1) / s;
P = 12;
G1 = 27 / (s + 200);
G2 = 5 / (s + 0.1);
#################

FAUX1 = minreal(P * G1);
FTLC1 = minreal(FAUX1 / (1 + FAUX1))
FAUX2 = minreal(FTLC1 * G2 * PI)
FTLCTOTAL = minreal(FAUX2 / (1 + FAUX2))

#usando feedback:2
ftlc1 = feedback(P*G1,1)
ftlc2 = minreal(feedback(ftlc1*G2*PI,1))



disp("termino el programa ")



