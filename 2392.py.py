n, m = input().split() #declaração do usuários
n = int(n)
m = int(m)

lista = [0 for i in range(n)] #criando a lista de tamanho n 

for i in range (m):
    
    p, d = input().split() #declaração do usuários para a lista
    p = int(p)
    d = int(d)
    
    p = p-1
    lista[p] = 1
    lado1 = p - d 
    while lado1 >= 0: #calculando as possibilidades para o lado 1
        lista[lado1] = 1
        lado1 = lado1 - d
        
    lado2 = p + d
    while lado2 < n:#calculando as possibilidades para o lado 2
        lista[lado2] = 1
        lado2 = lado2 + d

for i in lista:
    print(i)