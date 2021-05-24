x = int(input())
v = [int(i) for i in input().split()]
posicao = 0   
menor = int(v[0])
for i in range (1,  len(v)):
    if int(v[i]) < menor:
        menor =  int(v[i])
        posicao = i
   
print ('Menor valor: {}'.format(menor))
print ('Posicao: {}'.format(posicao))

