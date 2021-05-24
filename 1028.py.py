'''def mdc(a, b):
    return a if not b else mdc(b, a % b)
n = int(input())

for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(mdc(a, b))'''

def mdc(a, b):
    if(a % b == 0):
        return b
    else:
        return mdc(b, a % b)


n = int(input())

for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(mdc(a, b))