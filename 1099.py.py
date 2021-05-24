# -*- coding: utf-8 -*-
n = int(input())
d = 0
for i in range(1 , n + 1):
    x, y = input().split()
    x = int(x)
    y = int(y)
    soma = 0
    if x > y:
        for d in range(y+1, x):
            if d % 2 != 0:
                soma += d
    if x < y:
        for d in range(x+1, y):
            if d % 2 != 0:
                soma += d
    if x == y:
        soma = 0
    print(soma)
    
