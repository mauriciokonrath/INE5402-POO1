while True:
  try:
      frase = str(input()) #lendo a frase
      x = frase.replace(" ,", ",") #subtituindo o ( ,) por (,)
      y = x.replace(" .", ".") #subtituindo o ( .) por (.)     
      print(y) #imprimindo o resultado
   
  except EOFError:
    break
