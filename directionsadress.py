# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:38:14 2020

@author: Cristhian
"""

def direccion(calle,sect,cP,ref,numcasa):
    print("Su direccion es:\n",
          "Sector:",sect,"\n",
          "Calle:",calle,"\n",
          "Numero de casa:",numcasa,"\n",
          "Codigo postal:",cP,"\n",
          "Esta cerca de",ref)
    
print("Ingrese los datos a continuacion:\n")
calle=input("Ingrese la calle:\n")
sect=input("Ingrese sector de residencia:\n")    
cP=input("Ingrese codigo postal:\n")
numcasa=input("Ingrese el numero de casa:\n")
ref=input("Ingrese una referencia:\n")

direccion(calle,sect,cP,ref,numcasa)