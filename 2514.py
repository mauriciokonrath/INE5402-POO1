def mdc(a, b): #calculando o mdc
    if b == 0:
        return a
    y = mdc(b, a%b)
    return y


def mmc(a, b): #calculando o mmc
    z = a*b//mdc(a, b)
    return z

while True:
    try:
        m = int(input()) #lendo o ultimo alinhamento   

        L1, L2, L3 = map(int, input().split()) #lendo os valores 
        n = mmc(L1, mmc(L2, L3)) - m  #calculando o mmc dos valores e diminuindo com o ultimo alinhamento
        print(n) #imprimindo o resultado
        
    except EOFError:
            break


