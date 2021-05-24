n, c = input().split()
n = int(n)
c = int(c)
x = 0
cont = 0

for i in range (n): #enquanto n o programa vai se repetir
    s, e = input().split()
    s = int(s)
    e = int(e)
    x += e # o x vai somar as entradas de cada repetição
    x -= s # o x vai diminuir as saídas  de cada repetição
    if x > c: # se o x for maior que a capacidade o cont recebe 1 
        cont = 1 

if cont == 1: # se o cont for igual a 1 significa que a capacidade foi passada 
    print('S')
else:
    print('N')


