n = int(input())
dicionario = dict()
lista = list()
for i in range(n):
    idioma = str(input())
    traducao = input()
    dicionario[idioma] = traducao
    
m = int(input())
for i in range(m):
    nome = input()
    idioma_crian = str(input())
    
    print(nome)
    print(dicionario[idioma_crian])
    print()

