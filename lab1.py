# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:16:20 2020

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


testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = añobis(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")



