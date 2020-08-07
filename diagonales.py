# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:06:02 2020

@author: Cristhian
"""
from random import randint


fil=int(input("Numero de filas: "))
col=int(input("Numero de columnas: "))
vector=[[int() for ind0 in range(col)]for ind1 in range(fil)]

 
for f in range (fil):
    for c in range(col):
        vector[f-1][c-1]=randint(0,99)

for i in range (fil):
    
    print("\n")
    for j in range(col):
        print(vector[i-1][j-1],end=" ")

print("\n")
print("El valor de la diagonal principal de la matriz es: ") 

for i in range(fil):
    print("\n")
    for j in range (col):
        if i==j:
            print(vector[i-1][j-1],end=" ")
        else:
            print("0",end=" ")
            
print("\n")
print("El valor de la diagonal secuandaria de la matriz es: ")         
           
for i in range(fil):
    print("\n")
    for j in range (col):
        if i+j==(fil-1):
            print(vector[i-1][j-1],end=" ")
        else:
            print("0",end=" ")