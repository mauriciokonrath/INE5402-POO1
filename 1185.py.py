o = input()
matriz=[]

for i in range(3):
    matriz.append([])
    for j in range(3):
        x = float(input())
        matriz[i].append(x)
c = 3 
soma = 0
cont = 0
for i in range(2):
    c -=1
    for j in range(c):
        soma += matriz[i][j]
        cont += 1

if o == 'S':
    print('{}'.format(soma))

if o == 'M':
    med = soma / cont
    print('{:.1f}'.format(med)) 