# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:07:49 2020

@author: Cristhian
"""
from random import randint

def nmaymen():    
    auxiliar=int()
    vector=[int() for ind0 in range(30)]    
    for i in range (1,dim+1):
        vector[i-1]=randint(0,99)
        print("El valor de la posicion ",i,
              " es ",vector[i-1])
    for j in range(1,dim+1):
        for l in range(1,dim):
            if vector[l-1]<vector[l]:
                auxiliar=vector[l-1]
                vector[l-1]=vector[l]
                vector[l] = auxiliar
    for k in range(1,dim+1):
        print("El vector ordenado en la posicion ",
              k," es ",vector[k-1])
    
def nmenmay():
    auxiliar=int()
    vector=[int() for ind0 in range(30)]
    
    for i in range (1,dim+1):
        vector[i-1]=randint(0,99)
        print("El valor de la posicion ",i,
              " es ",vector[i-1])
    for j in range(1,dim+1):
        for l in range(1,dim):
            if vector[l-1]>vector[l]:
                auxiliar=vector[l-1]
                vector[l-1]=vector[l]
                vector[l] = auxiliar
    for k in range(1,dim+1):
        print("El vector ordenado en la posicion ",
              k," es ",vector[k-1])
    
def cmaymen():
    auxiliar=str()
    nombre=str()
    vector=[str() for ind0 in range(30)]


    for i in range (1,dim+1):
        print("Ingrese el nombre ",i)
        nombre=input()
        vector[i-1]=nombre
        print("El valor de la posicion ",i,
              " es ",vector[i-1])
  

    for j in range(1,dim+1):
        for l in range(1,dim):
            if vector[l-1]<vector[l]:
                auxiliar=vector[l-1]
                vector[l-1]=vector[l]
                vector[l] = auxiliar
    for k in range(1,dim+1):
        print("El vector ordenado en la posicion ",
              k," es ",vector[k-1])
        
def cmenmay():    
    auxiliar=str()
    nombre=str()
    vector=[str() for ind0 in range(30)]


    for i in range (1,dim+1):
        print("Ingrese el nombre ",i)
        nombre=input()
        vector[i-1]=nombre
        print("El valor de la posicion ",i,
              " es ",vector[i-1])
  

    for j in range(1,dim+1):
        for l in range(1,dim):
            if vector[l-1]>vector[l]:
                auxiliar=vector[l-1]
                vector[l-1]=vector[l]
                vector[l] = auxiliar
    for k in range(1,dim+1):
        print("El vector ordenado en la posicion ",
              k," es ",vector[k-1])

c=str(input("¿Digite 'si' si desea comenzar con la ejecucion? "))
while c=='si':

    dim=int(input("Ingrese una dimension para el vector: "))
    while dim<3 or dim>30:
        print("Dimension fuera de rango, digite un valor entre 3 y 30.\n")
        dim=int(input("Ingrese una dimension para el vector: "))

    a=str(input("Ingrese 'n' si va a ingresar numeros y 'c' si va a ingresar caracteres: "))

    if a == 'n':
        b=str(input("Ingrese 'm' si desea ordenarlos de mayor a menor o 'n' de menor a mayor: "))
        if b=='m':
            nmaymen()
    
        elif b=='n':
            nmenmay()
    
    
    elif a == 'c':    
        b=str(input("Ingrese 'm' si desea ordenarlos de mayor a menor o 'n' de menor a mayor: "))
        if b=='m':
            cmaymen()
    
        elif b=='n':
            cmenmay()
    c=str(input("¿Desea continuar con la ejecucion? "))
print("\n")    
print("Adios.")            
            
    
    
