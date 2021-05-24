
while True:
    try:
        n, r = input().split()
        maior = [x for x in range(1, int(n)+1)] #criando uma lista do 1 até o maior n
        voltaram = [int(x) for x in input().split()] #ler o número das pessoas que voltaram
        s = [x for x in maior if x not in voltaram] # verifica quais as pessoas não voltaram 
        if n == r: #se o n e o r forem iguais a variavel vai receber o asterisco e imprimi-lo 
            s = '*'
            print(s)
        else: #caso contrário
            for i in range(len(s)): #lendo o tamanho da lista que sobrou
                print(s[i], end=' ') #imprimindo uma ao lado da outra
            print()
        
    except EOFError:
        break