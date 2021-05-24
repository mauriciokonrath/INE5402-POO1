o = input()
matriz = []

for i in range(12):
    matriz.append([])
    for j in range(12):
        x = float(input())
        matriz[i].append(x)

soma = 0
m = 11
cont = 0
for i in range(1, 11):
    for j in range(m,12):
        soma += matriz[i][j]
        cont += 1
    if i < 5:
        m -= 1
    if i > 5:
        m += 1


if o == "S":
    print('{:.1f}'.format(soma))
else:
    media = soma / cont
    print('{:.1f}'.format(media))
print(matriz)