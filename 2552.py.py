   
while True:
    try:
        n, m = input().split()
        n = int(n)
        m = int(m)
        
        mat = [0] * 100
        tot = [0] * 100
        for i in range(100):
            tot[i] = [0] * 100
        
        
        for i in range(n):
            mat[i] = input().split()
            for j in range(m):
                tot[i][j] = 0
                
        for i in range(n): 
            for j in range(m):
                if mat[i][j] == '1': 
                    tot[i][j] = 9
                else:  
                    
                    vizin1 = i-1 
                    vizin2 = j
                    if vizin1 >= 0 and mat[vizin1][vizin2] == '1':
                        tot[i][j] += 1

                    vizin1 = i+1 
                    vizinhoJ = j
                    if vizin1 < n and mat[vizin1][vizin2] == '1':
                        tot[i][j] += 1
                        
                    vizin1 = i 
                    vizin2 = j-1
                    if vizin2 >= 0 and mat[vizin1][vizin2] == '1':
                        tot[i][j] += 1
                        
                    vizin1 = i 
                    vizin2 = j+1
                    if vizin2 < m and mat[vizin1][vizin2] == '1':
                        tot[i][j] += 1
                        
        for i in range(n):
            for j in range(m):
                print("%d" % (tot[i][j]), end='')
            print()
                
    except EOFError:
        break