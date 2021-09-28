# -*- coding: utf -8 -*
n = int(input())
a = [1, 2, 3, 4, 5, 6]

while (n > 0):
    n = n - 1
    m = []
    m.append(int(input()))
    x = input().split()
    for i in x:
        m.append(int(i))
    m.append(int(input()))
    orden = sorted(m)
    if (orden != a) or (m[0]+m[5] != 7) or (m[1]+m[3]!=7) or (m[2]+m[4] != 7):
        print('NAO')
    else:
        print('SIM')
