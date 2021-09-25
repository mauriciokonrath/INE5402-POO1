import math         
z = int(input())
for i in range (z):
    n = int(input())
    raiz = int(math.sqrt(n))
    for d in range (2, raiz + 1):
        if n % d == 0:
            print ('Not Prime')
            break
    else:
        print ('Prime')
        
        


'''z = int(input())
for i in range (z):
    n = int(input())
    primo = 0
    for d in range(1, n):
        if n % d == 0:
            primo += 1       
    if primo > 1:
      print("Not Prime")
    else:
      print("Prime")


a = int(input())
while a:
    n = int(input())
    if n <= n * 0.5 + 1:  
        print ("Prime")
    else:
        print ("Not Prime")
 

z = int(input())
for i in range (z):
    n = int(input())
    primo = 0
    for d in range(1, n):
        if n <= n * 0.5 + 1:   
            print("Prime")
            
        else:
            print("Prime")


z = int(input())
for i in range (z):  
    n = int(input())
    i = 2
    primo = 0
    while i <n  and primo == 0:
        if n%i==0:
            primo=1
            print ('Not Prime')
        i = i+1
    if primo ==0:
       print ('Prime')
        
 z = int(input())
for i in range (z):
    n = int(input())
    primo = 0
    for d in range(1, n):
        if n % d == 0:
            primo += 1       
    if primo > 1:
      print("Not Prime")
    else:
      print("Prime")


a = int(input())
while a:
    n = int(input())
    if (n == 1 or (n % 2 == 0 and n!=2 )or (n % 3 == 0 and n!=3 )or (n % 5 == 0 and n!=5 )):
        print ("Not Prime")
    else:
        print ("Prime")    


import math
n = int(input())
if ((n==0) or (n==1)):
    ehPrimo = False
else:
    ehPrimo = True
    fim = int(math.sqrt(n))
    for i in range (2, fim+1):
        if ((n%i) == 0 ):
            ehPrimo = False
            break
if (ehPrimo == True):
    print('Prime')
else:
    print('Not Prime')

import math       
z = int(input())
for i in range (z):
    n = int(input())
    raiz = int(math.sqrt(n))
    for d in range (2, raiz + 1):
        if n % d ==0:
            print ('Not Prime')
        else:
            print ('Prime')  

        
       
z = int(input())
for i in range (z):
    n = int(input())
    primo = 0
    for d in range(1, n):
        if n % d == 0:
            primo += 1       
    if primo > 1:
      print("Not Prime")
    else:
      print("Prime")
      
    
import math         
def eh_primo (n):
    raiz = int(math.sqrt(n))
    for d in range (2, raiz +1):
        if n % d ==0:
            return False
    return True      

z = int(input())
for i in range (z):
    numero = int(input())
    if eh_primo(numero):
        print ('Prime')
    else:
        print ('Not Prime')
       
       



import math  
z = int(input())
while z:
    n = int(input())
    raiz = int(math.sqrt(n))
    for d in range (2, raiz +1):
        if n % d ==0:
            print ('Not Prime')
        else:
            print ('Prime')

       
       
z = int(input())
for i in range (z):
    numero = int(input())
    if eh_primo(numero):
        print ('Prime')
    else:
        print ('Not Prime')       
     
       
import math         
def primo (n):
    raiz = int(math.sqrt(n))
    for d in range (2, raiz +1):
        if n % d ==0:
            return False
    return True      

z = int(input())
for i in range (z):
    numero = int(input())
    if primo(numero):
        print ('Prime')
    else:
        print ('Not Prime')     
'''       
        
     
        
        
