o = input()
matriz = []

for i in range(12):
    matriz.append([])
    for j in range(12):
        x = float(input())
        matriz[i].append(x)

soma = 0
menor = 1
maior = 11
cont = 0
for i in range(0,5):
    for j in range(menor,maior):
        soma += matriz[i][j]
        cont += 1
    menor += 1
    maior -= 1


if o == "S":
    print('{:.1f}'.format(soma))
else:
    media = soma / cont
    print('{:.1f}'.format(media))
