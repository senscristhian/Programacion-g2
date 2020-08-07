# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:12:39 2020

@author: Cristhian
"""
while True:
    x=input("Ingrese un numero: ")
    if x == 'q'  or x == 'quit':
        break
    else:
        x=int(x)
        y=1
        while True:
            print(y)
            y=y+1
            if y>x:
                break

         
    
