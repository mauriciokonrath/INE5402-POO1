# -*- coding: utf-8 -*-
import math
n, m, s = input().split() #lendo os valores do campo
n = int(n)
m = int(m)
s = int(s)

#precisamos calcular o angulo vizinho ao reto do local
#usando a fórmula para calcular a area do retangulo e usando a função atan para devolver o valor em radianos
grau1 = (math.atan(n/m))
grau1 = grau1 * 180 / 3.14 #multiplicando o valor radiano e depois dividindo por pi para retornar o valor em graus

hab_exerc1 = 0
hab_exerc2 = 0

for i in range(s):
    
    x, y, h = input().split() #lendo os valores da matriz
    x = int(x)
    y = int(y)
    h = int(h)

       
    if y != 0: #se o valor for 0 não poderá ser dividido, por isso a condição, ou seja, caso ele seja diferente de zero, os dois serão divididos
        grau2 = (math.atan(x/y))
    else: #caso seja igual a zero apenas devolvemos o valor de x
        grau2 = (math.atan(x))
    grau2 = grau2 * 180 / 3.14 #multiplicando o valor radiano e depois dividindo por pi para retornar o valor em graus
    
    if (grau2 < grau1): #se o angulo do grau1 for menor que do grau2 
        hab_exerc1 += h #somamos o valor de h para a habilidade do exército 1
    else: #caso contrário
        hab_exerc2 += h #somamos o valor de h para a habilidade do exército 2
    
print(hab_exerc1, hab_exerc2) #exibindo o nivel de habilidade de cada um
