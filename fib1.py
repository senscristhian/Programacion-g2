# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:58:03 2020

@author: Cristhian
"""



        
def fibonacci(n):
    a, b = 0,1
    while a <= n:
        print(a)
        c=a+b
        a=b
        b=c     
        
        
fibonacci(8)
            
            