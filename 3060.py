v = int(input()) #lendo os valores
p = int(input())

divisao = v // p #dividindo os valores
resto = v % p #determinandp o resto
parcela = [] #criando uma lista

for i in range(p): 
    parcela.append(divisao) #adicionando os valores da divisão na lista

tot = 0
if resto > 0: #se o resto for maior que 0
    for i in range(resto): #passando pelos valor do resto 
        parcela[tot] += 1 # somando ao tot e acrescentando na lista 
        tot += 1 #tot receb mais 1         

for p in parcela:#imprimindo o resultafo
    print(p) 
