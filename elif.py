# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:26:02 2020

@author: Cristhian
"""


num=input("Cual es el IPv4 numero ACL \n")
num=int(num)
if num>=1 and num<=99:
    print("Es ACL estandard")
elif num>=100 and num<=199:
    print("Es ACL extendida")
else:
    print("No es ACL")    
    