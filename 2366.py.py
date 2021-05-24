n, m = input().split()
n = int(n)
m = int(m)
p = list(map(int,input().split())) #criando a lista
p.append(42195) #acrescentando o ultimo elemento da lista
z = 0
for i in range(1, n+1): 
    if abs(p[i-1] - p[i]) > m: #diminuindo a posição anterior com a nova e usando o abs para remover o sinal negativo
        z = 1 #caso a subtração entre os dois ponto forem maiores que a média do atleta, x recebe 1
        
if z != 1: #se o z for diferente de 1 
    print ("S")
else: #se o z for igual a 1
    print ("N")
    
    