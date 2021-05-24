n, k = input ().split () #lendo os valores de teste
n = int(n)
k = int(k)

x = input().split() #lendo os horários de cada aluno
cont = 0

for i in range (n): 
    if x[i] <= '0': #se algum i do x for menor ou igual a 0 
        cont += 1 # cont recebe +1
        
if cont >= k: #se esse cont for maior o igual ao valor de k 
    print('YES') #imprime YES
else:      #caso contrario
    print('NO') #imprime não