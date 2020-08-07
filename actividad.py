# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:36:42 2020

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
  print("Bienvenido al sistema"+space+name+space+last+space+
        "tomando en cuenta que eres un niño"+space+
        "Hemos buscado lugares cerca de"+space+location+space+
        "Que te podrian interesar.")

elif age>12 and age<=17:
 print("Bienvenido al sistema"+space+name+space+last+space+
      "tomando en cuenta que eres un joven"+space+
      "Hemos buscado lugares cerca de"+space+location+space+
      "Que te podrian interesar.")
elif age>17 and age<=25:
  print("Bienvenido al sistema"+space+name+space+last+space+
      "tomando en cuenta que eres un adolesente"+space+
      "Hemos buscado lugares cerca de"+space+location+space+
      "Que te podrian interesar.")
elif age>25:
  print("Bienvenido al sistema"+space+name+space+last+space+
      "tomando en cuenta que eres un adulto"+space+
      "Hemos buscado lugares cerca de"+space+location+space+
      "Que te podrian interesar.")
else :
  print("ERROR")  
  
  


