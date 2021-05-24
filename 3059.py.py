n, l, f = input().split() #lendo os valores 
n = int(n)
l = int(l)
f = int(f)
pares = [0]*n #criando o tamanho da minha lista
cont = 0
pares = input().split()  #lendo os valores da minha lista
for i in range(n): #passando pelos valores da lista 
    for h in range(i+1): #passando pelo próximo valor de i
        pares[i] = int(pares[i]) #transformando para inteiro
        pares[h] = int(pares[h]) #transformando para inteiro
        if (pares[i] != pares[h]): #verificando se os números são iguais os diferentes
            if (pares[i] + pares[h] >= l and  pares[i] + pares[h] <= f): # quando eles forem diferentes, será elaborada a soma entre eles e então verificado se ela é maior ou igual ao l e se ela é menor ou igual ao f
                cont += 1 #caso as duas situações forem verdadeiras, cont receberá +1
print(cont)
    