# -*- coding: utf -8 -*
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)


if a>b and a<c:
    print (a)
elif a>c and a<b:
    print (a)

elif b>a and b<c:
    print (b)
elif b>c and b<a:
    print (b)

elif c>b and c<a:
    print (c)
elif c>a and c<b:
    print (c)

