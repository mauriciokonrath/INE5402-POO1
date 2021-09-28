n = int(input())
m = [x for x in range(1, int(n)+1)] #criando uma lista do 1 até o maior n
l = [int(x) for x in input().split()] #ler o número de peças que tem
s = [x for x in m if x not in l] # verifica quais as peças faltando de acordo com a lista feita na variavel m
for i in range(len(s)): #lendo o tamanho da lista que sobrou 
    print(s[i]) #imprimindo 

