cont1 = 0
cont2 = 0
x = int(input())
v = [int(i) for i in input().split()]
for i in range (0,  len(v)):
    if int(v[i]) == 1:
        cont1 += 1
    elif int(v[i]) == 0:
        cont2 += 1
        
if cont1 >= cont2:
    print('N')
else:
    print('Y')
