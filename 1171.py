def cont(numeros):
    x = enumerate(numeros)
    for i, j in x:
        if i == 0:
            print('{} aparece {} vez(es)'.format(j, numeros.count(j)))
        elif j != z:
            print('{} aparece {} vez(es)'.format(j, numeros.count(j)))
        z = j

n = int(input())
numeros = []
for i in range(n):
    x = int(input())
    numeros.append(x)
numeros.sort()
cont(numeros)
