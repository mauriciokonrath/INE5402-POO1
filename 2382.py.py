# -*- coding: utf -8 -*
import math

l, a, p, r = input().split()
l = int(l)
a = int(a)
p = int(p)
r = int(r)

diam = r+r
diag = math.sqrt((l*l) + (a*a) + (p*p)) # importar essa bibliotteca para tirar raiz

if diag <= diam:
     print('S')

else :
     print('N')


