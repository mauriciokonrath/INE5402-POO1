# -*- coding: utf-8 -*-
x = 0
contAlc = 0
contGas = 0
contDie = 0

while (x != 4):
    x = int(input())
    if (x == 1):
        contAlc = contAlc + 1
    elif (x == 2):
        contGas = contGas + 1
    elif (x == 3):
        contDie = contDie + 1
        
print ('MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}'.format( contAlc, contGas, contDie))