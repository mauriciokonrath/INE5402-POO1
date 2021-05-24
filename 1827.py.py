while True:
        try:
            n = int(input())
            matriz = []
            for i in range(n):
                matriz.append([])
                for j in range(n):
                    matriz[i].append('0') # matriz formada de zeros
            for i in range(n):
                matriz[i][i] = '2' #diagonal principal
            for i in range(n):
                matriz[i][n - 1 - i] = '3' #diagonal secundária
            for i in range(n // 3,n - n // 3):
                for j in range(n // 3,n - n // 3):
                    matriz[i][j] = '1' #parte interna
            matriz[n // 2][n // 2] = '4' #ponto central
            for i in range(n):
                mat = ''.join(matriz[i])
                print(mat)
            print()
        except EOFError:
            break


    