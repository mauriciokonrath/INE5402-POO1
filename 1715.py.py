n, m = input().split()
n = int(n)
m = int(m)
      
cont = 0
for i in range(n):
    matriz = input().split()
    if matriz.count('0') == 0:#contando as quantidades de 0, caso não tenha nenhum 0 soma +1
         cont += 1
                
            
print(cont)

