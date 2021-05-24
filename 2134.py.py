cont = 1
while True:
    try:
        n = int(input())
        menor = 11 #problemas
        reprov = []
        for i in range(n):
            aluno, nota = input().split()
            nota = int(nota)
            if nota == menor and reprov < aluno:
                reprov = aluno
                menor = nota
            elif nota < menor:
                reprov = aluno
                menor = nota

        print('Instancia %d' % cont)
        print(reprov)
        print()
        cont += 1

    except EOFError:
        break

