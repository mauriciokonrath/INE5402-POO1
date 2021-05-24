n, k = input().split()
n = int(n)
k = int(k)
alt = input().split() 

for i in range(n):
    alt[i] = int(alt[i])

pico = 0
vale = 0
numpicos = 0
numvales = 0
for i in range(1,n): 
    if alt[i] > alt[i-1]: 
        if not pico: 
            pico = 1
            vale = 0
            numpicos += 1 
            
    if alt[i] < alt[i-1]: 
        if not vale: 
            vale = 1
            pico = 0
            numvales += 1 

if numvales == k and numpicos == k: 
    print("eautiful")
else:
    print("ugly")
