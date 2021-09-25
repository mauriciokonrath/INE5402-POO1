while True:
    x = input().lower()
    word = x.split(' ') #formando a string
    if x == '*': #se a string for um *
        break
    for word in word:
        if word[0] != x[0]: #se algumas das iniciais forem diferentes
            print('N')
            break
    else:
        print('Y')
