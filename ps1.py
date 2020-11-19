# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 12:49:26 2020

@author: avanish.bidar
"""

#Problem set 1


#list of prime numbers
def prime(x):
    for i in range(2,x):
        if x%i == 0:
            break
    else:
        return True       
for x in range(1, 1000):
    if prime(x) == True:
        print(x)

#in the below code the summation of log(prime) is getting closer to the value n
from math import *
y= 0
n = 100000
def prime(x):
    for i in range(2,x):
        if x%i == 0:
            break
    else:
        return True       
for x in range(1, n):
    if prime(x) == True:
        y=y+log(x)
print(y)
print(n)
