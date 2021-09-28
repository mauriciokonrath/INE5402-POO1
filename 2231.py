temperatura =[10000]
while True:
    n, m =  input().split()
    n = int(n)
    m = int(m)
    teste = 1
    
    if n == m == 0:
        break
    
    for i in range(0, m):
        temperatura = int(input())
        soma = 0       
        soma += int(temperatura[i])
        
    maior = menor = soma
    for i in range (int(n)):
        x = soma//int(m)
        
        '''temperatura = int(input())
        soma1 = temperatura[i]
        soma2 = temperatura [i - (int(m))]
        soma += (soma1) - (soma2)
        if (soma > maior):
            maior = (soma/m)
        if (soma < menor):
            menor = (soma/m)
          
            
    
    print("Teste {}".format(teste))
    print("%d %d" % ((maior), (menor)))
    print()
    teste +=1'''
    print(x)















'''
caso = 0
while True:
    n, m =  input().split()
    n = int(n)
    m = int(m)
    soma = 0
    teste = 0
    temperatura = [10000]
    if n == m == 0:
        break
    
    temperatura = [int(input()) for i in range(n)]
    soma += temperatura
    maior = menor = soma
    print(soma)

    for i in range(n):
        
        soma = soma + temperatura[i] - temperatura[i-m]
        if (soma > maior):
            maior = soma
        if (soma < menor):
            menor = soma      
             
    teste += 1
    y = menor/m
    z = maior/m
    print("Teste {}".format(teste))
    print("%d %d" % ((y), (z)))
    print()
'''
