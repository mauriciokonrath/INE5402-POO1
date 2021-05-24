# -*- coding: utf-8 -*-

matriz = [list(map(int, input().split())) for i in range(3)] #recendo o valor da matrziz 3x3
soma = 0
if (matriz[0][0] == 0) + (matriz[1][1] == 0) + (matriz[2][2] == 0) == 0: #verifica se existe algum zero na diagonal principal
  soma = matriz[0][0] + matriz[1][1] + matriz[2][2] #soma o valor da diagonal principal, caso não tenha 0  
if (matriz[0][2] == 0) + (matriz[1][1] == 0) + (matriz[2][0] == 0) == 0: #verifica se existe algum zero na diagonal secundária
  soma = matriz[0][2] + matriz[1][1] + matriz[2][0] #soma o valor da diagonal secundária, caso não tenha 0 
for j in range(3):
  if (matriz[0][j] == 0) + (matriz[1][j] == 0) + (matriz[2][j] == 0) == 0: #verifica se existe algum zero nas colunas
    soma = matriz[0][j] + matriz[1][j] + matriz[2][j] #soma o valor das colunas , caso não tenha 0
for i in range(3):
  if (matriz[i][0] == 0) + (matriz[i][1] == 0) + (matriz[i][2] == 0) == 0: #verifica se existe algum zero nas linhas
    soma = matriz[i][0] + matriz[i][1] + matriz[i][2] #soma o valor das linhas, caso não tenha 0  
if soma == 0: #caso a a soma da matriz seja igual a 0
  for i in range(3):
    for j in range(3):
      soma += matriz[i][j] #a soma vai receber a propria matriz      
  soma //= 2 #matriz dividida por 2  
for _ in range(3):
  for i in range(3):
    for j in range(3):
      if matriz[i][j] == 0 and (matriz[i][0] == 0) + (matriz[i][1] == 0) + (matriz[i][2] == 0) == 1: #verifica a posição que se encontra o zero nas linhas
        matriz[i][j] = soma - matriz[i][0] - matriz[i][1] - matriz[i][2] #e desconta a soma anterior com o valor das posições        
      if matriz[i][j] == 0 and (matriz[0][j] == 0) + (matriz[1][j] == 0) + (matriz[2][j] == 0) == 1: #verifica a posição que se encontra o zero nas colunas
        matriz[i][j] = soma - matriz[0][j] - matriz[1][j] - matriz[2][j] #e desconta a soma anterior com o valor das posições       
for i in range(3): #imprimindo o resultado
  print(*matriz[i]) # usando o *, para desempacotar a lista e retornar todos os elementos em formato de matriz