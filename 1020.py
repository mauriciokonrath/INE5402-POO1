# -*- coding: utf -8 -*-

print ("Digite sua idade em dias:")
idade = int (input())
ano = idade//365
idade = idade - ano*365
mes = idade//30
idade = idade - mes * 30
dia = idade


print(ano, "ano(s)")
print(mes, "mes(es)")
print(dia, "dia(s)")
