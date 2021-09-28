n, s = input().split()
n = int(n)
s = int(s)
menor = s #variavel 'menor' recebe o valor do saldo antes dos cálculos
for i in range (n): #enquanto n, o programa vai se repetir
    a = int(input())
    s += a #o s vai somar ou diminuir as entradas de cada repetição
    if s < menor: #se o saldo for menor que a variavel 'menor'
        menor = s #então o menor vai receber o saldo final     
print (menor)

