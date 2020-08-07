# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:02:06 2020

@author: Cristhian
"""


x=int(input("Ingrese un numero: "))
i=0
y=1
while True:
    print(y)
    i+=y
    y+=1
    if y>x:
        break
print("El promedio es: ",i/x)    