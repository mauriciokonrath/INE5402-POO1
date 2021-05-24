n = int(input())
p, q, r, s, x, y = input().split()
p = int(p)
q = int(q)
r = int(r)
s = int(s)
x = int(x)
y = int(y)
i, j = input().split()
i = int(i)
j = int(j)

resultado = 0
for k in range(1,n+1): #Percorro os elementos da linha i e da coluna j
    Aik = (p * i + q * k) % x #Computo o valor da posição Aik
    Bkj = (r * k + s * j) % y #Computo o valor da posição Bkj
    resultado += Aik * Bkj #Acumulo a multiplicação do valor das posições Aik e Bkj
    
print(resultado)