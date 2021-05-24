o = input()
matriz=[]

for i in range(12):
    matriz.append([])
    for j in range(12):
        x = float(input())
        matriz[i].append(x)
c = 0
soma = 0
cont = 0
media = 0
for i in range(11,0,-1): #encontrando as posições
    c +=1
    for j in range(c,12):
        soma += matriz[i][j]
        cont += 1

if o == 'S':
    print('{}'.format(soma))

if o == 'M':
    media = soma / cont
    print('{:.1f}'.format(media)) 