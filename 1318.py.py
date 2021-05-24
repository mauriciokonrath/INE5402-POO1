while True:
    n, m = input().split()
    n = int(n)
    m = int(m)

    if(n == 0 and m == 0):
       break
    v = input().split()
    x = len(set([a for a in v if v.count( a ) > 1])) #usando o set para identificar a quantidade de números distintos e usando o len para contar os repetidos
    print( x )