#!/usr/bin/python2.6
# -*- coding : utf-8 -*
""" module multipli contenant la fonction table """

def table (nb=3 , max=15):
  """ Fonction affichant la table de multiplication par nb de 1 * nb jusqu 'a max * nb """
  nb = input("entrez le nombre a multiplier: ") 
  max = input("Entre le nombre d'occurence: ")
  i = 1
  while i <= max:
        print (nb, "X", i, "=", nb * i)
        i += 1
# test de la table dans le module
if __name__ == "__main__":
#if __name__ == " __main__ ":
   table() 
