#!/usr/bin/python2.6
# -*- coding : utf-8 -*
# Programme testant si une annee, saisie par l'itulisateur est bissextile ou non 
annee = input("Saisissez une annee : ") # On attend que l'utilisateur fournisse l'annee qu'il desire tester
annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre
 
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'annee saisie est bissextile.")
else:
    print("L'annee saisie n'est pas bissextile.")
