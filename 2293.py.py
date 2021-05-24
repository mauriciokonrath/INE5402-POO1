n, m = input().split()
n = int(n)
m = int(m) 
matriz = []

for i in range(n):
            linha = input().split()
            matriz.append(linha)

for i in range(n):
    soma = 0
    for j in range(m):
        soma += int(matriz[i][j])
    if i == 0:
        total = soma
    elif soma > total:
        total = soma

for j in range(m):
    soma = 0
    for i in range(n):
        soma += int(matriz[i][j])
    if soma > total:
        total = soma

print(total)