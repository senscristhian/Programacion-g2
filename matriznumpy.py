# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:09:21 2020

@author: Cristhian
"""


import numpy as np
matrix=np.array([[1,2,3,4,5],[5,6,7,8,9,10]])
print(matrix)
print("\n"*2)
unos=np.ones((8,4))
print(unos)
print("\n")
ceros=np.zeros((5,5))
print(ceros)
print("\n" )
aleatorios=np.random.random((5,5))
print(aleatorios)
print("\n")
ept=np.empty((4,3))
print(ept)
print("\n")
full=np.full((2,5),8)
print(full)
print("\n")
espacio1=np.arange(1,100,10)
print(espacio1)
print("\n")
espacio2=np.linspace(1,100,10)
print(espacio2)