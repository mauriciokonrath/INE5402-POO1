# -*- coding: utf -8 -*

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if (a+b)>c and (b+c)>a and (a+c)>b:
    
    if ( a != b and a != c and b != c ):
        print('Valido-Escaleno')
        if(a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==b**2+a**2):
             print('Retangulo: S')
        else :
            print('Retangulo: N')
    elif (a == b and a == c):
        print('Valido-Equilatero')
        if(a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==b**2+a**2):
             print('Retangulo: S')
        else :
            print('Retangulo: N')
    elif (a == b or a == c or b == c):
        print('Valido-Isoceles')
        if(a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==b**2+a**2):
             print('Retangulo: S')
        else :
            print('Retangulo: N')

else:
    print ('Invalido')
    
