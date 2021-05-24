# -*- coding: utf-8 -*-

cont = 1
while (True):
    x = int(input())
    if (x != 0 ):
        i = x // 50
        j = (x % 50) // 10   
        k = (x%10) // 5
        l = (x%5)//1
    else:
        break 
    print('Teste %d' % cont)
    print ('{:.0f} {:.0f} {:.0f} {:.0f}'.format (i, j, k, l))
    print ()
    cont +=1