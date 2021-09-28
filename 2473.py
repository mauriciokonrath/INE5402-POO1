f = input().split() #lendo os valores de flavio
sort = input().split() #lendo os valores sorteados
cont = 0 #declarando a variavel cont

for i in range(6): #lendo a lista com todos os 6 valores desde o primeiro até o sexto
    for h in range(6): #lendo a lista com todos os 6 valores desde o primeiro até o sexto
        if sort[h] == f[i] : #comparando as duas listas para ver quais elementos são iguais 
            cont += 1 #caso tenha algum soma + 1
            
if (cont < 3): #caso a soma seja menor que 3 imprime azar
    print("azar")            
elif (cont == 3): #caso a soma seja igual a 3 imprime terno
    print("terno")
elif (cont == 4): #caso a soma seja igual a 3 imprime quadra
    print("quadra")
elif (cont == 5): #caso a soma seja igual a 3 imprime quina
    print("quina")
elif (cont == 6): #caso a soma seja igual a 3 imprime sena
    print("sena")
