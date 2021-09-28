l, c = input().split()
l = int(l)
c = int(c)

a, b = input().split()
a = int(a) -1
b = int(b) -1


mat = [0]*l
for i in range(l):
    mat[i] = input().split()
    

while True:
    mat[a][b] = '2'
    
    nextA = -1
    nextB = -1
    
    vizin1 = a-1
    vizin2 = b
    if vizin1 >= 0 and mat[vizin1][vizin2] == '1': 
        nextA = vizin1
        nextB = vizin2

    vizin1 = a +1
    vizinhoJ = b
    if vizin1 < l and mat[vizin1][vizin2] == '1': 
        nextA = vizin1
        nextB = vizin2
          
    vizin1 = a
    vizin2 = b +1
    if vizin2 < c and mat[vizin1][vizin2] == '1': 
        nextA = vizin1
        nextB = vizin2
         
    vizin1 = a
    vizin2 = b -1
    if vizin2 >= 0 and mat[vizin1][vizin2] == '1': 
        nextA = vizin1
        nextB = vizin2
        
    if nextA == -1:
        print("%d %d" % (a+1, b+1))
        break
    
    a = nextA
    b = nextB
    
    
    
