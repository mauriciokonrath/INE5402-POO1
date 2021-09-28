# -*- coding: utf-8 -*-
n = int(input())
matriz = []
compl = []
colunas = [[] for x in range(n)]

for i in range(n):
    matriz.append(list(map(int, input().split())))
    compl.append(sum(matriz[i]))
    for j in range(n):
        colunas[j].append(matriz[i][j])
comparadorColuna = []
for j in range(n):
    comparadorColuna.append(sum(colunas[j]))

if compl.count(max(compl)) == 1:
    num_errado = max(compl)
    num_certo = min(compl)
    l_errado = compl.index(num_errado)
else:
    num_certo = max(compl)
    num_errado = min(compl)
    l_errado = compl.index(num_errado)

if comparadorColuna.count(max(comparadorColuna)) == 1:
    c_errado = comparadorColuna.index(max(comparadorColuna))
else:
    c_errado = comparadorColuna.index(min(comparadorColuna))

errado = matriz[l_errado][c_errado]
certo = errado + num_certo - num_errado
print(certo, errado)
