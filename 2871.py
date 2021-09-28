      
while True:
    try:
    
        n, m = input().split() #lendo os valores 
        n = int(n)
        m = int(m)
        
        matriz = []

        for i in range(n): #lendo os valores da matriz 
            linha = input().split()
            matriz.append(linha)
            
        soma = 0
        for i in range(n): #somando todos os valores da matriz
            for j in range(m):
                soma += int(matriz[i][j])

           
        
        sacas = soma//60 #saca vai ser dividida por 60 caso seja maior 
        litros = soma % 60 # e o resto vai ser recebido pelos litros
        
        
        print("{} saca(s) e {} litro(s)". format(sacas, litros)) #imprimindo resultado
                
    except EOFError:
        break
