teste = 1
while True:
    a, v = input (). split ()
    a = int(a)
    v = int(v)
    if a == 0 and v == 0:
        break
    lista = [0]*a #tamanho da lista será multiplicada pelo a
    for i in range (v):
        x, y =  input (). split ()
        x = int(x)
        y = int(y)
        lista[x-1] += 1 #somando 1 em cada valor de x digitado
        lista[y-1] += 1 #somando 1 em cada valor de y digitado

    z = max(lista) #vendo qual é o maior número das somas
    nm = [str(i + 1) for i in range(len(lista)) if lista[i] == z] #identificando quais dos elementos é o maior
    print('Teste %d' % teste)
    teste += 1
    print(' '.join(nm), '') #usado o join para montar a resposta com o tamanho adequado, removendo as aspas e os colchetes
    print()
