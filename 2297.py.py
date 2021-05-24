cont = 1
while True: #enquanto for verdade
    q = 0
    p = 0
    z = int(input())
    if z == 0: #caso o número de tentativas seja igual a 0 o programa será encerrado
        break
    print('Teste {}'.format(cont))
    cont +=1 #soma os números de testes
    for i in range (z):
        a, b = input().split()
        a = int(a)
        b = int(b)
        q += a #soma o número de figurinhas de Aldo
        p += b #soma o número de figurinhas de Beto
    if q > p: #se a quantidade de Aldo for maior que a quantidade de Beto, Aldo ganha
          print('Aldo')
          print()
          
    elif p > q:#se a quantidade de Aldo for menor que a quantidade de Beto, Beto ganha
          print('Beto')
          print()
          



