# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:34:31 2020

@author: Cristhian
"""


tamano=10
vector=[]

for j in range(10,0,-1):
    vector.append(j)
for a in range(1,tamano+1):
    for b in range(1,tamano):
        if vector[b-1]>vector[b]:
            auxiliar=vector[b-1]
            vector[b-1]=vector[b]
            vector[b]=auxiliar
for k in range(1,tamano+1):
    print(vector[k-1],end="")    
