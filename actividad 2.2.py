# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:16:37 2020

@author: Cristhian
"""


print("Bienvenido al sistema")
name=input("¿Cual es tu nombre?")
last=input("¿Cual es tu apellido?")
location=input("¿Donde vives?")
age=input("¿Cual es tu edad?")
age=int(age)
space=(" ")

if age>0 and age<=12:
      car=("niño")
elif age>12 and age<=18:
      car=("adolecente")
elif age>18 and age<=25:
      car=("joven")
elif age>25:
      car=("adulto")
else:
     car=("adulto mayor")
  
print("Bienvenido al sistema"+space+name+space+last+space+
         "tomando en cuenta que eres un"+space+car+space+
         "Hemos buscado lugares cerca de"+space+location+space+
         "Que te podrian interesar.")