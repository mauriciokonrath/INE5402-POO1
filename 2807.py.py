def fibonacci(n):

    fib = [1, 1] #ultimos termos
    for x in range(2, 41):        
        fib.append(fib[x-1] + fib[x-2])
    fib.sort(reverse=True) #invertindo
    
    palavra = ''
    for x in fib[41 - n:]:
        palavra += str(x) + ' '
    palavra = palavra[:-1]
    print(palavra)
    
    
n = int(input())
fibonacci(n)
