# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 15:17:37 2020

@author: Cristhian
"""


def añobis(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
    
    
    
def meses(año,mes):
    if mes>=1 and mes<=12:
        mes=str(mes)
        if añobis(año) is True:          
            m={
                   "1":"31","2": "29","3": "31",
                   "4": "30","5": "31","6": "30",
                   "7": "31","8": "31","9": "30",
                   "10": "31","11": "30","12": "31"
                   }

            return int(m[mes])

        elif añobis(año) is False:
            m={
                   "1":"31","2": "28","3": "31","4": "30",
                   "5": "31","6": "30","7": "31","8": "31", 
                   "9": "30","10": "31","11": "30","12": "31"
                   }

            return int(m[mes])            
     
    else:
        return None  
        


def diadelaño(año,mes,dia):

    if mes==1 :
        return dia
    elif mes>1 and mes<=12:
        cont=0
        for i in range(1,mes):
            a=meses(año,i)
            print(a)
            cont+=a
        a=meses(año,mes)
        return cont+dia
            
        
            
            
           
print(diadelaño(2020,3,1))
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        