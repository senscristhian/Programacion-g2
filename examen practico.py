# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:05:43 2020

@author: Cristhian
"""

vector=[int() for ind0 in range(10)]
gas=0
liq=0
sol=0
s=0
print("--ANALISIS DE TEMPERATURA DEL AGUA--")
a=int(input("Ingrese la cantidad de temperaturas [1,10]: "))

while a>10 or a<1:
    print("ERROR")
    a=int(input("Ingrese la cantidad de temperaturas [1,10]: "))
    
for i in range (1,a+1):
    print("Temperatura ",i," en °C: ")        
    vector[i-1]=int(input("")) 
    s=s+vector[i-1]
    
    
for j in range(1,a+1):
    if vector[j-1]>=100:
        gas+=1
    elif vector[j-1]>0 and vector[j-1]<100:
        liq+=1
    elif vector[j-1]<=0:
        sol+=1
   
print("RESUMEN DEL ANALISIS DE MUESTRAS DEL AGUA")         
        
print("\n")
print("Cantidad de muestras solidas: ",sol)
print("Cantidad de muestras liquidas: ",liq)
print("Cantidad de muestras gaseosas: ",gas)    
print("\n")


prom=s/a
print("Temperatura promedio °C: ",prom)

far=(prom * 9/5)+32
print("Temperatura promedio en °F: ",far)
    