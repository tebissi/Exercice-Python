#!/usr/bin/python2.6
a = 25
b = 12
if a > 0:
   a += b
   b = a + b
   print('a =', a, 'b =', b) 
# forme comple if elif else
ali = 16
if ali >= 18:
   print('ali est majeur')
else:
   print('ali est mineur') 
    
# L'instruction elif

c = -0
if c < 0:
   print('c est negatif')
elif c > 0:
   print('c est positif')
else:
   print('c est neutre')

# les booleens

age = 2
majeur = False
if age >= 18:
   majeur = True
else:
   print(majeur)
