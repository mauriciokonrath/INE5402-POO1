
while True:
    o = int(input())
    
    if o == 0:
        break
    
    matriz = []
    for i in range (0, o):
        matriz.append([])
        for j in range(o):
            matriz[i].append(0)
    
    matriz[0][0] = 1
    
    for i in range (0,o):
        if i >= 1:
            matriz[i][0] = matriz[i - 1][0] * 2
        for j in range(1, o):
            matriz[i][j] = matriz[i][j-1] * 2
              
    

   
    for i in range(o):
        for j in range(o):
            matriz[i][j] = str(matriz[i][j])
            T = len(str(matriz[o-1][o-1]))
            while len(matriz[i][j]) < T:
                matriz[i][j] = ' ' + matriz[i][j]
        x = ' '.join(matriz[i])
        
        print(x)
    print()
