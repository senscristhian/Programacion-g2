# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:48:26 2020

@author: Cristhian
"""

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()