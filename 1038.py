# -*- coding: utf -8 -*

x, quant = input().split()
x = int(x)
quant = int(quant)


if x == 1:
    a = (quant * 4.00)
    print('Total: R$ {:.2f}'.format(a))
elif x == 2:
    a = (quant * 4.50)
    print('Total: R$ {:.2f}'.format(a))
elif x == 3:
    a = (quant * 5.00)
    print('Total: R$ {:.2f}'.format(a))
elif x == 4:
    a = (quant * 2.00)
    print ('Total: R$ {:.2f}'.format(a))
elif quant == 5:
    a = (quant * 1.50)
    print('Total: R$ {:.2f}'.format(a))






