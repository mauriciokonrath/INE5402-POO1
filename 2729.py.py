def remove_repetidos(compras):
    compras = sorted(set(compras))    
    print(*compras)
    
    
x = int(input())
for i in range(x):
    compras = input().split()
    remove_repetidos(compras)





    