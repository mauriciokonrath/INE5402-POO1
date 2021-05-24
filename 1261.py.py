while True:
    try:
        a, b = map(int, input().split())
        dicio = {}
        for _ in range(a):
            cargo, salario = input().split()
            salario = int(salario)
            dicio[cargo] = salario
        for _ in range(b):
            
            soma = 0
            
            while True:
                frase = input()
                if frase == '.':
                    break
                frase = frase.split()
                for word in frase:
                    if word in dicio:
                        soma += dicio[word]
            
            print(soma)

    except EOFError:
