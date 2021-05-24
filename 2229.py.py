cont=1
while True:
    n = int(input())
    if n == -1 :
        break
    else:
        d = ((1+(2**n))*(1+(2**n)))
        
        print('Teste %d' % cont)
        print(d)
        print()
        cont += 1
        
