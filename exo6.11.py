#!/usr/bin/python2.6
# -*- coding : utf-8 -*
# Homme ou femme
from math import *
a = raw_input("entrez le cote a: ")
a = float(a)
b = raw_input("entrez le cote b: ")
b = float(b)
c = input("entrez le cote c: ")
c = float(c)
if a == b == c :
   print("le triangle est equilaterale")
elif (a == b or a == c or b == c) and (a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + c**2):
   print("le triangle est isocele rectangle")
elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + c**2:
   print("le triangle est rectangle")
      
elif a == b or a == c or b == c:
 print("le triangle est isocele")

else:
 print("le triangle est quelquonque")
