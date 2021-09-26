def par(x):
    x.sort()
    for elem in x:
        print(elem)
        
def impar(x):
    x.sort(reverse=True)
    for elem in x:
        print(elem)

x = int(input())
pares = []
impares = []
for i in range(x):    
    a = int(input())
    if a % 2 == 0:
        pares.append(a)
    else:
        impares.append(a)
    
par(pares)
impar(impares)
