while True:
    contjoao = 0
    contmaria = 0
    n = int (input())
    if n == 0:
        break
    v = input().split ()
    for i in range (0 , n):
        v [i] = int ( v [i ])
        if v[i] == 1:
            contjoao += 1
        elif v[i] == 0:
            contmaria += 1
    
    print('Mary won {} times and John won {} times'.format(contmaria, contjoao))
