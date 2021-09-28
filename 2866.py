x = int(input())
for i in range(x):
    c = input()
    s = ''.join(i for i in c if i.islower()) #trasnformando para string e identificando as letras maiusculas para removelas
    s = s[::-1] #convertendo o resultado de trás para frente
    print(s)
