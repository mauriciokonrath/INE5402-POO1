while True:
    x = int(input())
    if x == 0:
        break
    a = 0
    for i in range (x):
        ci, vi = input().split()
        ci = int(ci)
        vi = int(vi)
        if (vi % 2 == 0):
            a += vi
        else:
            a += vi -1
    z = (a//4)

    print(z)




