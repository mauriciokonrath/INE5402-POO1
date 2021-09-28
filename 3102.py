x = int(input()) 
for i in range (x):#enquanto o x digitado o programa será executado
    area = 0
    x1, y1, x2, y2, x3, y3 = input().split()  
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    x3 = int(x3)
    y3 = int(y3)
    area = abs(x1 * (y2 -y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2 #fórmula para a area de um triangulo com tais coordenadas
    print ('{:.3f}'.format(area))
