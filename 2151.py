c = int(input())

matriz = [0] * 100 

for num_teste in range(1, c+1): 
    m, n, x, y = input().split()
    m = int(m)
    n = int(n)
    x = int(x) -1 
    y = int(y) -1
    
    for i in range(m): 
        matriz[i] = input().split()
        for j in range(n):
            matriz[i][j] = int(matriz[i][j]) 
    
   
    for i in range(m):
        for j in range(n):
            distancia = max(abs(i-x), abs(j-y))
            if distancia > 8:
                matriz[i][j] += 1
            else: 
                matriz[i][j] += 10 - distancia
    
    
    print("Parede {}:".format(num_teste))
    for i in range(m):
        print("%d" % (matriz[i][0]), end='')
        for j in range(1,n):
            print(" %d" % (matriz[i][j]), end='')
        print()
