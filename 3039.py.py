n = int(input()) #lendo o número de nomes declarados
contF = 0 #declarando variáveis
contM = 0
for i in range(n): #fazer até o numero total dos nomes declarados acima 
    nome, g = input().split() #lendo o nome e o genero do individuo
    nome = str(nome)
    g = str(g)

    if g == 'F': #se o genero for F, soma mais um
        contF += 1
    elif g == 'M': #se o genero for M, soma mais um
        contM += 1
        
print((contM),'carrinhos') #imprimindo os resultados
print((contF),'bonecas')