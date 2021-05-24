n = int(input()) #lendo a quantidade de textos
for i in range(n):
    texto = input().split() #lendo o texto
    palavra = input() #palavra a ser procurada
    posicao = 0 
    lista = [] #criando uma lista para as posições das palavras
    for j in texto:
        if j == palavra: #caso a palavra seja igual a procurada
            lista.append(posicao) #adiciona a posição na lista
        posicao += len(j) + 1 #somando 1 ao tamanho para calcular a posição
    if len(lista) == 0: #se a palavra nao estiver no texto é acrescentado "-1" 
        lista.append(-1)
    print(*lista, sep = ' ') # imprimindo o resultado