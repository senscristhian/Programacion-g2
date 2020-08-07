# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:47:05 2020

@author: Cristhian
"""

año = int(input(' '))

def añobis(año):
    
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return 'True'
            else:
                return 'False'
        else:
            return 'True'
    else:
        return 'False'
    
print(añobis(año))    