# -*- coding: utf-8 -*-
x = int(input())
for _ in range(x):
    m, n = map(int, input().split())
    dicionario = dict()
    for i in range(m):
        japones = input()
        traducao = input()
        dicionario[japones] = traducao
    for _ in range(n):
        letra = input().split()
        new = ""
        for i in range(len(letra)):
            if letra[i] in dicionario:
                new += dicionario[letra[i]] + " "
            else:
                new += letra[i] + " "
        new = new.strip()
        print(new)
    print()
