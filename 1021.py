# -*- coding: utf-8 -*-
x = float(input())

a100 = x // 100 
x = x - (a100 * 100)
b50 = x // 50
x = x - (b50 * 50)
c20 = x // 20
x = x - (c20 * 20)
d10 = x // 10
x = x - (d10 * 10)
e5 = x // 5
x = x - (e5 * 5)
f2 = x // 2
x = x - (f2 * 2)
g1 = x // 1
x = x - (g1 * 1)
h050 = x // 0.5
x = x - (h050 * 0.5)
i025 = x // 0.25
x = x - (i025 * 0.25)
j010 = x // 0.10
x = x - (j010 * 0.10)
k005 = x // 0.05
x = x - (k005 * 0.05)
l001 = x * 100

print('NOTAS:')
print('{:.0f} nota(s) de R$ 100.00'.format(a100))
print('{:.0f} nota(s) de R$ 50.00'.format(b50))
print('{:.0f} nota(s) de R$ 20.00'.format(c20))
print('{:.0f} nota(s) de R$ 10.00'.format(d10))
print('{:.0f} nota(s) de R$ 5.00'.format(e5))
print('{:.0f} nota(s) de R$ 2.00'.format(f2))
print('MOEDAS:')
print('{:.0f} moeda(s) de R$ 1.00'.format(g1))
print('{:.0f} moeda(s) de R$ 0.50'.format(h050))
print('{:.0f} moeda(s) de R$ 0.25'.format(i025))
print('{:.0f} moeda(s) de R$ 0.10'.format(j010))
print('{:.0f} moeda(s) de R$ 0.05'.format(k005))
print('{:.0f} moeda(s) de R$ 0.01'.format(l001))
