CP = [0] * 1001 #criando a lista
while True:
    p,n,c = input().split()
    p = int(p)
    n = int(n)
    c = int(c)
   
    if p == n == c == 0:
        break
    
    maior = 0
    cont = 0
    
    while cont <= p: 
        CP[cont] = 0
        cont += 1
        
    for h in range(n): 
        PD = input().split() 
        for i in range(p):
            if PD[i] == '1': 
                CP[i] += 1
            else: 
                if CP[i] >= c:
                    maior += 1  
                CP[i] = 0
    
   
    for i in range(p):
        if CP[i] >= c:
            maior += 1

    print(maior)

