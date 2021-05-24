while True:
    try:
        n, q = input().split()
        n = int(n)
        q = int(q)
        notas = []
        for i in range(n):
            nota = int(input())
            notas.append(nota)
        notas.sort(reverse=True)
        for i in range(q):
            posição = int(input())
            print(notas[posição - 1])        
    except EOFError:
        break    
        
        
    