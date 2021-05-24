while True: #enquanto for verdade o programa será executado
    try:
        x, y = input().split()  
        x = int(x)
        y = int(y)
           
        a=(x * 12)//360 #O x vai ser multiplicado pela metade de horas que um dia possui e depois dividido pela quantidade de segundos em uma hora
        b=(y * 60)//360 #O y vai ser multiplicado pelo 60 que signifa os minutos de uma hora e depois dividido pelos segundos que uma hora tem
        
        print("{:0>2}:{:0>2}". format(a, b)) 
    except EOFError:
        break
