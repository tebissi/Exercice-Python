#!/usr/bin/python2.6
# -*- coding : utf-8 -*
# encode une liste
print("Encoder une liste")
liste = []
a = 0
while a != "" :
  a = raw_input("Entre un nombre:")
  if a != "":
     liste.append(a)
  else:
     print(liste)


