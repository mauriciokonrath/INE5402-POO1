# -*- coding: utf-8 -*-
n= int(input())
for i in range(n + 1):
    if(i%2 == 0 and i>0):
        x = i**2
        print("{}^2 = {}".format(i, x))
