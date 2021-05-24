while True:
    n, m = input().split()
    n = int(n)
    m = int(m)
    
    if n == m == 0:
        break
    
    c = 4
    comp = []
    for i in range(n):
        comp.append([int(x) for x in input().split()])


    for i in range(n): 
        p = comp[i].count(1)
        if p == m:
            c = c - 1
            break

    questao = [0] * m
    for i in range(n):
        for j in range(m):
            if comp[i][j] == 1:
                questao[j] += 1
                
    if questao.count(0) > 0:
        c = c - 1
    
    for j in range(m):
        if questao[j] == n:
            c = c - 1
            break


    for i in range(n):
        p = comp[i].count(0)
        if p == m:
            c = c - 1
            break

    print(c)