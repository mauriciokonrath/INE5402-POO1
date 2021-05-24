def chuva(n,m):
    for i in range(n): 
        linha = input() # lendo o valor de cada linha
        matriz.append(linha) # adicionando a linha na matriz 
        gotas_process.append([]) # cria uma nova linha na matriz de gotas a serem processadas
        
        if i % 2 != 0: # caso a linha seja impar
            prateleiras.append([]) # nova linha na matriz prateleiras
            pratele = 0 # pratele inicia com 0
            cont = 0 # numero de prateleiras
            for j in range(m): 
                if linha[j] == '#' and not pratele: # se uma prateleira está iniciando
                    pratele = 1 # pratele recebe 1
                    prateleiras[i].append([j]) # acrescenta na posição de início
                    cont += 1 # soma um na contagem
                elif linha[j] == '.' and pratele: # se uma prateleira acabou
                    pratele = 0 #pratele recebe 0
                    prateleiras[i][cont - 1].append(j - 1) # acrescenta a posição de fim
        else:
            prateleiras.append(0) #  se a linha for par adiciona 0 porque não tem prateleleiras 
            
    for i in range(m):
        if matriz[0][i] == 'o': # se tiver uma gota  
            gotas.append([0, i]) # Adiciona a sua posição na lista
            break
          
    while len(gotas) > 0: #enquanto tiver gotas 
        while gotas[0][0] < n: # se a gota não tenha chegado ao fim da matriz
            if gotas[0][1] not in gotas_process[gotas[0][0]]: # se não tiver gotas  na posição
                gotas_process[gotas[0][0]].append(gotas[0][1]) # é colocado a posição na lista de gotas já processadas
            if gotas[0][0] < n - 1: # se a posição não for a penultima 
                # se a posição abaixo tem uma prateleira ou uma gota
                if matriz[gotas[0][0] + 1][gotas[0][1]] == '#' or gotas[0][1] in gotas_process[gotas[0][0] + 1]:
                    break 
            gotas[0][0] += 1 # desce a linha da gota
            
        #se a linha for par 
        if gotas[0][0] % 2 == 0 and gotas[0][0] < n - 1: # e se tiver uma prateleira abaixo
            for p in prateleiras[gotas[0][0] + 1]: # para cada prateleira abaixo
                if gotas[0][1] >= p[0] and gotas[0][1] <= p[1]: # se tiver uma gota acima da prateleira
                    for i in range(p[0], p[1] + 1): # posição acima da posição que a prateleira 
                        if i not in gotas_process[gotas[0][0]]: # se nao tiver uma gota naquela posição
                            gotas_process[gotas[0][0]].append(i) # é colocado a posição na lista de gotas já processadas
                    # adiciona uma nova gota na esquerda 
                    gotas.append([gotas[0][0], p[0] - 1])
                    # adiciona uma nova gota na direita
                    gotas.append([gotas[0][0], p[1] + 1])
        gotas.remove(gotas[0]) # remove a gota processada
        
    for i in range(n): 
        linha = [] 
        for j in range(m): 
            if j in gotas_process[i]: # se tiver uma gota
                linha += 'o' # adiciona a gota na matriz
            else: 
                linha += matriz[i][j] # se não, coloca o caractere original
        print(*linha, sep ='') # imprimindo resultado





n, m = map(int, input().split()) # lendo a linha e a coluna da matriz
matriz = [] 
prateleiras = [] # matriz de prateleiras
gotas = [] 
gotas_process = [] # gotas a serem processadas
chuva(n, m)
