# -*- coding: utf-8 -*-
tape = {}
days = 0


length, n = (int(x) for x in input().split())
seeds = (int(x) for x in input().split())

for x in range(1, length + 1):
    tape[x] = 0

for s in seeds:
    tape[s] = 1

while not all(tape.values()):
    for s in [x for x in tape.keys() if tape[x]]:
        j = s - 1
        k = s + 1
        if j > 0:
            tape[j] = 1
        if k < length + 1:
            tape[k] = 1
    days += 1
print(k)
print(length)

print(tape)
print(days)
'''


compr, n = input().split()
compr = int(compr)
n = int(n)
pos_anterior = 0
maxi = pos_anterior-1

pos = input().split()  
for i in range(n): 
    diferenca = (int(pos[i]) - pos_anterior)//2  
    if (diferenca>maxi):
        maxi = diferenca
    pos_anterior = int(pos[i])

if (compr - pos_anterior > maxi):
    maxi = compr - pos_anterior
    
print(maxi)
'''        
