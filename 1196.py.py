# -*- coding: utf-8 -*-

while True:
    try:
        x = input()
        novo = ''
        for i in x:
            lista = " `1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./ " #criando a lista dos caracteres do teclado
            if i == ' ':
                novo += i
            else:
                novo += lista[lista.index(i)-1] #chamando o valor anterior ao da letra na lista
        print(novo)
    except EOFError:
        break

