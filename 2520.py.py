while True:
    try:
        n, m = input().split()
        n = int(n)
        m = int(m)
        matriz = []
        for i in range(n):
            linha = input().split()
            matriz.append(linha)
            
        cont2x = 0
        cont2y = 0
        cont1x = 0
        cont1y = 0
        
        for i in range(n):
            for j in range(m):
                if (matriz[i][j] == '2'):
                    cont2x = j
                    cont2y = i
                elif (matriz[i][j] == '1'): 
                    cont1x = j
                    cont1y = i
        if (cont2x > cont1x): 
            x = cont2x - cont1x
        else:
            x = cont1x - cont2x
            
        if (cont2y > cont1y):
            y = cont2y - cont1y
        else:
            y = cont1y - cont2y
            
            
        print(x + y)
                    

    except EOFError:
        break

