x = int(input()) #ler o valor digitado pelo usuário
if (x <= 10): #se o valor for menor ou igual a 10, o tot receberá 7
    tot = 7 #o tot receberá 7
    
elif (x >= 11 and x <= 30): #se o valor for maior ou igual a 11 e menor ou igual a 30
    tot = 7 + (x - 10) #o tot vai receber o 7 mais o valor do x subtraido pelo 10 que é maior valor entre        

elif (x >= 31 and x <= 100) :#se o valor for maior ou igual a 31 e menor ou igual a 100
    tot = 7 + 20 + (2 * (x - 30))#o tot vai receber 27 pelo consumo até 30m3, e por fim somará o valor do x subtraido pelo 30 que é o maior valor entre e que foi multiplicado pelo 2  
 
elif (x >= 101): #se o valor for maior ou igual a 101
    tot = 7 + 20 + 140 + (5 *(x-100))#o tot vai receberá 167 que é a soma dos anteriores, e somará o valor do x subtraido pelo 100 que é o maior valor entre e que foi multiplicado pelo 5  
    
print(tot)
    