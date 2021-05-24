o = input()
matriz=[]

for i in range(12):
    matriz.append([])
    for j in range(12):
        x = float(input())
        matriz[i].append(x)
c = 11
soma = 0
cont = 0
media = 0
for i in range(11,0,-1):
    for j in range(0, c):
        soma += matriz[i][j]
        cont += 1
    c -= 1

if o == 'S':
    print('{}'.format(soma))

if o == 'M':
    media = soma / cont
    print('{:.1f}'.format(media))      
    