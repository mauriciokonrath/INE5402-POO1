x = int(input())
for i in range(x):
    a,b = input().split()
    comb = '' #transformando em string
    if (len(a) > len(b)): #se o tamanho da variável a for maior que b
        for i in range(len(b)):
            comb += a[i] #o comb vai receber a letra na posição 0 de a e depois a letra na posiçã 1 de a e assim por diante
            comb += b[i] #o comb vai receber a letra na posição 0 de b e depois a letra na posiçã 1 de b e assim por diante
        comb += a[len(b):] #verificando o resto que falta e adicionando ao final
        
    elif(len(a) <= len(b)): #se o tamanho da variável a for menor ou igual a b
        for i in range(len(a)):
            comb += a[i] #o comb vai receber a letra na posição 0 de a e depois a letra na posiçã 1 de a e assim por diante
            comb += b[i] #o comb vai receber a letra na posição 0 de b e depois a letra na posiçã 1 de b e assim por diante
        comb += b[len(a):]  #verificando o resto que falta e adicionando ao final
    print(comb)     
    
