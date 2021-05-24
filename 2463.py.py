vidas = [] 
bom = [0] * 50000 #declarando as possibilidades de salas
prox = [0] * 50000 #declarando as possibilidades de salas
n = int(input()) #numero de salas
vidas = input().split() #quantidade de vidas
    
bom[0] = prox[0] = vidas[0] #iniciando todos igualmente

if (int(vidas[0]) < 0): #verificando se a primeira posição é menor que 0  
    bom[0] = 0 #se for, atribuimos 0
    prox[0] = 0 #se for, atribuimos 0

for i in range(n):
    soma = int(prox[i-1]) + int(vidas[i]) #somando as distancias
    if ( soma >= 0 ):  #se a soma não for negativo ou 0, então o prox vai receber essa soma
        prox[i] = soma
    else:
        prox[i] = 0 #inicializando em 0 
    bom[i] = bom[i-1] #bom recebe a posição anterior 

    if prox[i] > bom[i-1]: #caso o prox for maior que o bom 
        bom[i] = prox[i] #então o bom, vai receber o prox, pois a "vida" será maior
x = 0
x = bom[n-1] #passando a melhor posição para a variavel x
print(x) #imprimindo