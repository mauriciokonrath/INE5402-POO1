while True:
    a, d = input().split()
    a = int(a)
    d = int(d)
    if a == 0 and d == 0:
        break
    b = []
    c = []
    
    dist_atacantes = [int(i) for i in input().split()]
    dist_defensores = [int(j) for j in input().split()]
    dist_atacantes.sort()
    dist_defensores.sort()
        
    if (dist_atacantes[0] >= dist_defensores[1]):
        print('N')
    else:
        print('Y') 
