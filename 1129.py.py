while True:    
    num = int(input())
    if num == 0:  #caso seja igual a 0
        break
    for cont in range(num): #lendo os valores da lista
        n = input().split()
        cont = "*" #declarando as variaveis 
        z = 0
        for i in range(0, 5):
            a = int(n[i]) #definindo como inteiro
            if a <= 127: #caso algum elemento da lista seja menor ou igual a 127
                cont = i + 1
                z = z+1
        #localizando suas posições
        if(z > 1):
            cont = "*"
        if cont == 1: #caso o cont seja igual a 1 ele recebe A
            cont = "A"
        elif cont == 2: #caso o cont seja igual a 2 ele recebe B 
            cont = "B"
        elif cont == 3: #caso o cont seja igual a 3 ele recebe C
            cont = "C"
        elif cont == 4: #caso o cont seja igual a 4 ele recebe D
            cont = "D"
        elif cont == 5: #caso o cont seja igual a 5 ele recebe E
            cont = "E"
        print(cont)
