#!/usr/bin/python2.6
# -*- coding : utf-8 -*
# encode une liste
print("Encoder une liste")
a = [ii for ii in range(0,32)]
b = 0
i = 0
print(a)
while i <= 31:
    if ((a[i] %3) == 0) & ((a[i] %5) == 0) :   
       b = b + a[i]
    i += 1
print(b)
  
