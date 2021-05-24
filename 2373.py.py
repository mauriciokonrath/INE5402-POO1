x = int(input())
cont = 0
for i in range (x):
    l, c = input().split()
    l = int(l)
    c = int(c)
    
    if (l>c):
       cont += c
    
print (cont)
        