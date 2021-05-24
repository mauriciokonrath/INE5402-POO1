m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31,30, 31]
while True:
    try:
        mes, dia = input().split()
        mes = int(mes)
        dia = int(dia)
        soma = 0

        for i in range(mes - 1):
            soma += m[i]

        soma += dia
        x = 360 - soma
    
        if (mes == 12 and dia == 25):
            print ('E natal!')
        elif (mes == 12 and dia == 24):
            print ('E vespera de natal!')
        elif (mes == 12 and dia >=26 and dia < 32 and dia != 0):
            print ('Ja passou!')
        elif mes > 0 and mes <= 12 and dia < 32 and dia != 0:
            print("Faltam %d dias para o natal!"%(x))
    except EOFError:
        break
        
