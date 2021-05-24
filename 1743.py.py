x = input (). split ()
y = input (). split ()

for i in range (len(x)): #converter para inteiro
    x[i] = int(x[i])
for i in range (len(y)): #converter para inteiro
    y[i] = int(y[i])       
if x[0] == y[0] or x[1] == y[1] or x[2] == y[2] or x[3] == y[3] or x[4] == y[4]:        
    print('N')
else:
    print('Y')

