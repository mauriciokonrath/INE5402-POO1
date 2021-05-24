x = int(input())
nome = []
for i in range(x):
    s, p, k, m = input().split()
    s = str(s)
    p = int(p)
    k = int(k)
    m = int(m)
    
    nome.append((-int(p), -int(k), int(m), s))
nome.sort() #coloca na ordem quem é o maior
print(nome[0][-1])
