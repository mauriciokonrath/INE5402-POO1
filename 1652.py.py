l, n = input().split()
l = int(l)
n = int(n)
A = [0] * 21
B = [0] * 21

for i in range(0, l):
    A[i], B[i] = input().split() 

for h in range(0, n):
    a = input()
    
    acheiNoVetor = 0
    for i in range(0,l):
        if A[i] == a:
            print(B[i]) 
            acheiNoVetor = 1
            break
    
    ult = a[-1]
    ult2 = a[-2]

    if acheiNoVetor == 0:
        ult = a[-1]
        ult2 = a[-2]
        if ult == 'y':
            if (ult2 == 'a')  or (ult2 == 'e') or (ult2 == 'i') or (ult2 == 'o') or (ult2 == 'u'):
                print(a + 's')
            else:
                final = a[:-1]
                print(final + 'ies')
        
        elif ult == 'o' or ult == 's' or (ult2 == 'c'and ult == 'h') or (ult2 == 's'and ult == 'h') or ult == 'x':
            print(a + 'es')
        
        else:
            print(a + 's')