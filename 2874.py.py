while True:
    try:
        n = int(input())
        x = ""
        for h in range(n):
            a = input().strip()            
            m = 1 
            b = 0 
            for i in range(len(a)-1, -1, -1): 
                if a[i] == '1': 
                    b += m
                
                m = m * 2 
            x += chr(b)

        print(x)
    except EOFError:
        break