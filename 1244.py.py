def ordena(frase):
    for i in range(len(frase)):
        print(frase[i], end = '') #imprimindo lado a lado
        if i != len(frase) - 1: 
            print(' ', end = '')
    print() 

n = int(input())
for i in range(n):
    frase = input().split()
    frase.sort(key = len, reverse=True)
    
    ordena(frase)
