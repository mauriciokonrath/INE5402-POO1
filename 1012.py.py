# -*- coding: utf -8 -*-

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

tri = ((a*c)/2)
cir = (3.14159*(c**2))
trap = (((a+b)* c)/2)
quad = (b**2)
ret = (a*b)

print ("TRIANGULO: %.3f" % (tri))
print ("CIRCULO: %.3f" % (cir))
print ("TRAPEZIO: %.3f" % (trap))
print ("QUADRADO: %.3f" % (quad))
print ("RETANGULO: %.3f" % (ret))