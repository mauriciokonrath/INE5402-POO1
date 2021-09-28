while True:
    jingle = {'W' : 1, 'H' : 1/2, 'Q' : 1/4, 'E' : 1/8, 'S' : 1/16, 'T' : 1/32, 'X' : 1/64}
    compasso = input()
    if compasso == '*':
        break
    sep = [x for x in compasso.split('/') if x] #separa a string no /
    cont = 0
    for conjunto in sep:
        duracao = 0
        for i in conjunto:
            duracao += jingle[i] #somando até fechar 1
            if duracao > 1:
                break
        if duracao == 1:
            cont += 1

    print(cont)
