'''p, n = input().split()

alt = int(p[0])
canos = [int(c) for c in input().split()]
resultado = "YOU WIN"
for i in range(len(canos) - 1):
    diferenca = abs(canos[i+1] - canos[i])

    if diferenca > alt:
        resultado = "GAME OVER"
        break

print(resultado)
'''
p, ncano = input().split()
ncano = int(ncano)
alt = int(p[0])
n = [int(x) for x in input().split()]
x = "YOU WIN"
for i in range(ncano - 1):
    diferenca = abs(n[i+1] - n[i])

    if diferenca > alt:
        x = "GAME OVER"

print(x)