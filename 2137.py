def ordena(x):
    x.sort()
    for elem in x:
        print(elem)
        
while True:
    try:
        x = int(input())
        ordem = []
        for i in range(x):    
            ordem.append(input())            
        ordena(ordem)
    except EOFError:
        break
