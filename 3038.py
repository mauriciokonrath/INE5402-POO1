# -*- coding: utf-8 -*-
while True:
  try:
    f = input() #lendo a string
    a = f.replace("@", "a") #usando o replace para substituir o @ pelo a
    b = a.replace("&", "e") #usando o replace para substituir o & pelo e
    c = b.replace("!", "i") #usando o replace para substituir o ! pelo i
    d = c.replace("*", "o") #usando o replace para substituir o * pelo o
    e = d.replace("#", "u") #usando o replace para substituir o # pelo u
    print(e) #imprimindo a resposta final   
  except EOFError:
    break
