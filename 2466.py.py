matriz = []
n = int(input())
matriz = input().split()

while len(matriz) != 1:
   topo = []
   for i in range(len(matriz)-1):
      if matriz[i] == matriz[i+1]:
          topo.append(1)
      else:
          topo.append(-1)
   matriz = topo[:]
if topo[0] == 1:
    print('preta')
else:
    print('branca')