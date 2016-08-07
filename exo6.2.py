#!/usr/bin/python2.6
# -*- coding : utf-8 -*
# Ecrivez un programe qui calcule le perimetre et l'air d'un trianagle
# dont, les 3 cotes sont fourni par l'utilisateur
from math import *
print("calcul ddu perimetre et  l'air d'un triangle")
a = raw_input("entrer la logueur du cote a: ") 
a = float(a)
b = raw_input("entrer la logueur du cote b: ") 
b = float(b)
c = raw_input("entrer la logueur du cote c: ") 
c = float(c)
d = ( a + b + c ) / 2 
print("perimetre du triangle est ", a + b + c)

s = sqrt(d * (d-a) *  (d-b) * (d-c))
print("surface du traingle", s)


