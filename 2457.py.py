'''letra = str(input())
frase = input()
numfrase = 0.0

resultado = frase.count(letra)
numfrase = frase.count(" ") + 1

x = (resultado * 100) / numfrase
print('{:.1f}'.format(x))
'''




letra = input()
frase = input().split()
numfrase = 0.0
for i in frase:
    if letra in i:
        numfrase += 1

x = len(frase)
numfrase = (numfrase / (x/100))

print('{:.1f}'.format(numfrase))






