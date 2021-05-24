time=0
a = -1 #declarando a variavel como negativa
x = int(input())
for i in range (x):
    z = int(input())
    if(a != -1 and z - a < 10): #Se a variavel 'a' for verdadeira e a declaração do usuário juntamente com a variável 'a' for menor que os dez segundo o programa será executado,caso contrario ele somará 10 
            time -= 10 - (z - a) #Assim a variavel time vai receber o calculo, onde será descontado o momento em que o individuo entrou na escada
    a = z #a variavel 'a' vai receber a ultima declaração do usuário 
    time += 10 #E por fim o time vai receber os 10 segundos de diferença


print(time)





