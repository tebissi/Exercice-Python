#!/usr/bin/python2.6
# -*- coding : utf-8 -*
# calcul de la longueur du pendule
from math import *
print("calcul de la periode d'une pendule")
L = raw_input("entrer la logueur du pendul: ") 
L = float(L)
g = 10
T = 2 * pi * (sqrt(L/g))

print("la periode du pendule est: ", T)


