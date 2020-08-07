# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:40:20 2020

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
                 

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):   
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")  
	result = meses(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")


	
    