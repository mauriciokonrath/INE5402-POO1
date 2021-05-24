while True:
    try:
        original = dict()
        sala = dict()
        cont = 0
        tot = 0
        n = int(input())
        if n == 0:
            break
        for i in range(n):
            nome, ass_original = input().split()
            original[nome] = ass_original
            
        m = int(input())
        for i in range(m):
            nome_aluno, ass_aula = input().split()
            sala[nome_aluno] = ass_aula

        for i in sala.keys():
            cont = 0
            for j in range(len(sala[i])):
                if sala[i][j] != original[i][j]:
                    cont += 1
            if cont > 1:
                tot += 1

        print(tot)
        
    except EOFError:
        break