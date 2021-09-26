while True:
    try:
        d = [0] * 62
        e = [0] * 62
        total = 0
        
        x = int(input())
        
        for i in range(29, 62):
            d[i] = 0
            e[i] = 0

        for i in range(x):
            m, l = input().split()
            if l == 'E':
                e[int(m)] += 1
            else:
                d[int(m)] += 1
        
        for i in range(29, 62):
            if d[i] < e[i]:
                total += d[i]
            else:
                total += e[i]
        print(total)            
    except EOFError:
        break      


