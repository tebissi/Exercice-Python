#!/usr/bin/python2.6
# -*- coding : utf-8 -*

annee = input("entrez une annee: ")
try:
   annee = int(annee)
except SyntaxError:
   print("Erreur lors de la conversation")
