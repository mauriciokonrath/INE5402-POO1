# -*- coding: utf-8 -*-
cont = [0]
for i in range (1, 101):
    cont.append( i*i +cont[i-1])
while True:
    n = int(input())
    if (n==0):
        break
    print(cont[n])

    