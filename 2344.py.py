x = int(input()) #ler o valor digitado pelo usuário
if (x == 0): #se o valor for 0 ele vai exibir E
    print("E")
elif (x >= 1 and x <= 35): #se o valor for maior que 1 e menor que 35 ele vai exibir D
    print("D");
elif (x >= 36 and x <= 60): #se o valor for maior que 36 e menor que 60 ele vai exibir C
    print("C")
elif (x >= 61 and x <= 85): #se o valor for maior que 61 e menor que 85 ele vai exibir B
    print("B")
else : #caso não seja nenhuma das opçoes acima ele vai exibir A
    print("A")