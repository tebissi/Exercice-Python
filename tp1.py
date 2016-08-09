#!/usr/bin/python2.6
an = input("entree une valeur:")
print(an)
type(an)
an = int(an)
bissextile = False
if an % 400 == 0:
   bissextille = True
if an % 4 == 0 and an % 100 !=0:
    bissextile = True
else:
    bissextile = False
if bissextile == True:
    print(an,"est une annee bissextile")
else:
    print(an," n'est pas une annee bissextile")
          
      
