# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:35:27 2020

@author: Cristhian
"""


res=0
n=input("Ingrese un numero ")
n=int(n)
for i in range(1,n+1,2):
    print(i)
    res +=i
print("el resultado de la suma de 1 hasta ",n," es igual a: ",res)