# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:03:04 2020

@author: Cristhian
"""

inicio=int(input("Contador inicial: "))
final=int(input("Contador final: "))

contador=int(1)
control=int(10)
while control<=inicio:
    contador=contador+1
    control=control*10  
dif=final-inicio
dec=pow(10,(contador-1))

if dif<0:
    print("Error: El contador final es menor que el inicial")
    while final<inicio:        
        final=final+dec    
    print("Contador final: ",final)
    
imp=int(input("Impresora (1. B/N, 2. Color): "))
    
print("Impresiones: ",final-inicio)

if imp==1:
    print("Costo: $",(final-inicio)*0.06)
elif imp==2:
    print("Costo: $",(final-inicio)*0.12)    