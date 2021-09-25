o = input()
soma = 0
cont = 0
matriz = []

for i in range(12): #recebendo oas valores da matriz 12x12
    matriz.append([])
    for j in range(12):
        x = float(input()) 
        matriz[i].append(x)
        
for i in range(12):
    for j in range(12):
        if((i >= 7) and (i + j) >= 12 and (j < i)): #somando os valores abaixo da linha 7 até a a ultima linha, e o j precisa ser menor que o i, pois as linhas vão aumentando de tamanho enquando vai descendo
          soma += matriz[i][j] #somando os valores da matriz
          cont += 1 #cont receb um para fazer a média
      
if o == "S": #se for igual s imprime a soma
    print('{:.1f}'.format(soma))
else: # senão faz  a media e imprime ela
    media = soma / cont #fazendo a média
    print('{:.1f}'.format(media))
