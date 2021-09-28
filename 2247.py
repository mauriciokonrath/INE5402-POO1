'''cont = 1

while (True):
    x = int(input())
    if x == 0:
        break 
    total = 0
    while (x):
        j, k = input().split()
        j = int(j)
        k = int(k)
        total += j
        total -= k
        
        print('Teste %d' % cont)
        print (total)
        cont += 1
 '''       

cont = 1
while True:
    x = int(input())
    if x == 0:
        break
    toal = 0
    print('Teste %d' % cont)
    cont += 1
    while x:
        x -= 1
        j, k = input().split()
        j = int(j)
        k = int(k)
        toal += (j - k)
        print(toal)

    print()
