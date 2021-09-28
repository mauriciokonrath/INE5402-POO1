n = int(input())
hexa = str(input())
tradu = bytes.fromdec(hexa) #transformando cófigo hexadecima, usando a tabela ascii
asciis = tradu.decode("ASCII")
print(asciis)
