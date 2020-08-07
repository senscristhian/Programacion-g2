# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:50:31 2020

@author: Cristhian
"""

dato=int(input("Ingrese un numero: "))
i=1
j=0
while i <= dato:
    print(i)
    j+=i
    i+=1
print("El promedio de los numeros del 1 al ",dato,"es: ",
      j/dato)    
