while True:
    n = int(input())
    soma = 0
    teste = 1
    for _ in (0, n):
        c = input().split()
        for i in range (0 , len (c)):
            c[i] = int(c[i])
        
        
        contar0 = c.count(c[0])
        contar1 = c.count(c[1])
        contar2 = c.count(c[2])
        contar3 = c.count(c[3])
        contar4 = c.count(c[4])
      
        
         #regra 1   
        if (c[0]==c[1]-1) and (c[1]==c[2]-1) and (c[2]==c[3]-1) and (c[3]==c[4]-1):
                soma = 200 + c[0]

        #regra 2
        if contar0 == 4 or contar1==4 or contar2 == 4 or contar3 == 4 or contar4 ==4:
                soma = 180 + c[1]
    
        
        #regra 3
        elif (contar0 == 3 or contar1==3 or contar2 == 3 or contar3 == 3 or contar4 == 3) and (contar0 == 2 or contar1==2 or contar2 == 2 or contar3 == 2 or contar4 == 2):
                soma = 160 + c[4]

        
        #regra 4
        elif (contar0 == 3 or contar1==3 or contar2 == 3 or contar3 == 3 or contar4 == 3) and (contar0 != contar1 or contar0 != contar2 or contar0 != contar3 or contar0 != contar4 or contar1 != contar2 or contar1 != contar3 or contar2 != contar3 or contar3 != contar4):
                soma = 140 + c[0]
        
        
        #regra 5
        elif ((contar0 == 2 and contar1==2 or contar2 == 2 or contar3 == 2 or contar4 == 2)):
            if (c[0] > c[3]):
                soma = (3 * c[0]) + (2* c[4]) + 20
            else: 
                soma = (3*c[3])+(2*c[0])+20

       
        elif (((c[0]==c[1] or (c[0]==c[2]) or (c[0]==c[2]) and (c[3]==c[4]))  and c[2]==c[3])):
            if (c[0]>c[2]): 
                soma = 3*c[0]+2*c[2]+20
            else:
                soma = 3*c[3]+2*c[1]+20


        elif ((c[1]==c[2] and c[3]==c[4])): 
            if (c[1]>c[3]):
                soma = 3*c[1]+2*c[3]+20
            else:
                soma = 3*c[3]+2*c[1]+20

        #regra  6
        elif (c[0]==c[1] or c[1]==c[2]): 
            soma = c[1]
    
        elif (c[2]==c[3] or c[3]==c[4]): 
            soma = c[3]
          
        print('Teste', teste)
        print(soma)
        print()
        teste += 1