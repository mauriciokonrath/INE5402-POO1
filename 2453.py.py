#x = input()
'''
original = input()
removed = original.replace("p", "")
print(removed)

'''
frase = input()
fim = '' #montando a string
for i in frase.split(): #separando cada frase e vendo o tamando dela
    for x in range(1, len(i), 2): #contando de dois em dois e removendo as letras começando do da primeira letra
        fim += i[x] #passando a determinada letra para a variavel fim 
    fim += ' '#juntando as palavras
print(fim[:-1])

