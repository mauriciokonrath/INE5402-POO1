x = int(input()) #lendo o valor
if x % 2 == 0: #caso o número seja par, soma mais dois a ele
    x += 2
    print(x)
else: #caso ele seja ímpar, soma somente um
    x += 1
    print(x)