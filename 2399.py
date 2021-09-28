n = int(input())
encont = [0 for i in range(n)] #criar um lista que receba todos os valores digitados
for i in range(n):
    tabu = int(input())
    if tabu == 1 and (i) > 0: #quando houver no tabuleiro algum elemento que seja igual a 1 e a posição é menor que zero
        encont[i-1] += 1 #somando um na na posição anterior
    if tabu == 1 and (i+1) < n: #quando o valor for 1 e a próxima posição for menor que o próprio n
        encont[i+1] += 1 #somando um na próxima posição
    if tabu == 1: #quando o valor digitado no tabuleiro for igual a 1
        encont[i] += 1 #somando um na posição definida

for x in encont: #exibindo a lista
    print (x)






