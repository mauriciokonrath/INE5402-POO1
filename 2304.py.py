i, n = input().split()
i = int(i)
n = int(n)

D = i
E = i
F = i

for x in range(n):
    a = input().split()
    
    
    if a[0] == 'C': #em caso de compra
        a[2] = int(a[2])
        if a[1] == 'D':
           D -= (a[2])
        elif a[1] == 'E':
           E -= (a[2])
        elif a[1] == 'F':
           F -= (a[2])
           
    elif a[0] == 'V': #em caso de venda
        a[2] = int(a[2])
        if a[1] == 'D':
           D += (a[2])
        elif a[1] == 'E':
           E += (a[2])
        elif a[1] == 'F':
           F += (a[2])
           
    elif a[0] == 'A': #em caso de aluguel
        a[3] = int(a[3])    
        if a[1] == 'D' and a[2] == 'E':
           D += (a[3])
           E -= (a[3])
        elif a[1] == 'D' and a[2] == 'F':
           D += (a[3])
           F -= (a[3])
        elif a[1] == 'E' and a[2] == 'D':
           E += (a[3])
           D -= (a[3])
        elif a[1] == 'E' and a[2] == 'F':
           E += (a[3])
           F -= (a[3])
        elif a[1] == 'F' and a[2] == 'D':
           F += (a[3])
           D -= (a[3])
        elif a[1] == 'F' and a[2] == 'E':
           F += (a[3])
           E -= (a[3])
        
print(D, E, F)