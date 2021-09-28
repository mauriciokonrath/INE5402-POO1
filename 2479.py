def ordena(x):
    x.sort()
    for elem in x:
        print(elem)

'''        
def comportamento(comport, contmais, contmenos):

    if comport == '+':
        contmais += 1
    elif comport == '-':
        contmenos += 1
    print('Se comportaram: {} | Nao se comportaram: {}'.format(contmais, contmenos))
'''        
    

n = int(input())
nomes = []
contmais = 0
contmenos = 0
for i in range(n):
    comp, nome = input().split()
    nomes.append(nome)
    
    if comp == '+':
        contmais += 1
    elif comp == '-':
        contmenos += 1  
    
  
ordena(nomes)
print('Se comportaram: {} | Nao se comportaram: {}'.format(contmais, contmenos)) 
