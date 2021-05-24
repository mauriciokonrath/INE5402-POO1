from datetime import date #importando a blibloteca datetime, podendo assim manipular as datas
dia1, mes1 = input().split()
dia1 = int(dia1)
mes1 = int(mes1)

dia2, mes2 = input().split()
dia2 = int(dia2)
mes2 = int(mes2)

a = date(2021, mes1, dia1)#atribui a variavel 'a' o mes e o dia desejados, foi utilizado o ano de 2021 pois se trata de um ano não bissexto
b = date(2021, mes2, dia2)#atribui a variavel 'b' o mes e o dia desejados, foi utilizado o ano de 2021 pois se trata de um ano não bissexto
d = b - a #fazemos a diferença entre as datas, subtraindo-as
print(d.days) #imprimimos o resultado então, utilizando o argumento days, referente aos dias

