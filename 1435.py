while True:
    o = int(input())
    
    if o == 0:
        break
    
    matriz = []
    for i in range (0, o):
        matriz.append([])
        for j in range(0,o):
            matriz[i].append(0)
    
    if o % 2 == 0:
        t = o//2
    else:
        t = 1 + o//2       
    menor = 0
    maior = o
    cont = 0
    for k in range(0,t):
            cont += 1
            for i in range(menor,maior):
                
                for j in range(menor,maior):
                    matriz[i][j] = cont
            menor += 1
            maior -= 1
    for i in range(o):
        resp = ''
        for j in range(o):
            resp += " %3d" %matriz[i][j]
        print(resp[1:])
    print("")
  
        
    
    
    
