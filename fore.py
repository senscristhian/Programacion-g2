# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:10:28 2020

@author: Cristhian
"""
router=[]
switch=[]
lista=["R1","R2","R3","R4","S1","S2","True"]
for i in lista:
    if "R" in i:
        switch.append(i)
    else:
        router.append(i)
    
print(switch)
print(router)