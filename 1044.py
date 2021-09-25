# -*- coding: utf -8
a, b = input().split()
a = int(a)
b = int(b)

if (a % b == 0 ):
    print('Sao Multiplos')
elif (b % a == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
    
