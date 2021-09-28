while True:
    n = int(input())
    if n == 0:
        break
    v = input().split()
    for i in range(n): #transformando o vetor em inteiro
        v[i] = int(v[i])
    a = sorted(v)
    inicio = 0
    z=0
    for inicio, i in enumerate(v): #uso do enumerate para enumerar a lista
        if i == a[n-2]: #encontrando o penultimo item da lista
            z = inicio + 1 #somando mais 1 no tamanho da lista
            print(z)
  
