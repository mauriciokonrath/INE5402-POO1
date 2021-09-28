n, m = input().split()
n = int(n)
m = int(m)
matriz = []

for i in range(n): #lendo a matriz
    matriz.append(input())

resp = 'S' #começando como se a resposta fosse positiva, e apartir dai verificamos se ocorre alguma irregularidade
cond_2 = None
cond_1 = 0

for i in matriz:
    elem = [int(c) for c in i.split()] #lendo cada linha da matriz

    if cond_1: #verifica se na linha só existe zeros
        if any(elem): #ele se torna verdadeiro quando encontra um número após sequencia de zeros
            resp = 'N' #recendo o valor 'N'
            break

    if cond_2 is not None: # Se a condição 2 for verdadeira
        if elem[cond_2]: #se não tiver nenhum zero na linha
            resp = 'N'  #recendo o valor 'N'
            break
        
        elif cond_2 > 0 and any(elem[:cond_2]): #verifica se existe um zero na ordem adequada 
            resp = 'N' #recendo o valor 'N'
            break
        
    #utilizando a função any para verificar se a sequencia é verdadeira
    if any(elem): #verifica a quantidade de zeros em uma linha
        for y in range(0, len(elem)): #percorre a linha para encontrar o zero
            if elem[y]:
                cond_2 = y #caso encontre, ou não um zero retorna o valor de y
                break
    else: #se a linha for composta somente de zeros, retorna o valor 1 
        cond_1 = 1

print(resp)
