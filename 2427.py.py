l = int(input())
tot = 4 #número de pedaços divididos primeiramente
while(l/2 >= 2): #enquanto a divisão do lado for maior ou igual a 2 ele executará 
    l = l/2 #número de divisões até chegar ao que se pede 
    tot = tot * 4 #por fim, é multiplicado por 4 todas as vezes que foi feito divisões
print(tot)

