# import numpy as np
import math as m

tole = 1e-10
amplitude = 1e-10
contador = 0
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = b - a
limit_itera = 150


def f(x):
    f = x*x*x - x*x + 2
    return f


x_inicial = (a + b) / 2


while( c > amplitude or m.fabs(f(x_inicial) > tole)):
    if (f(a) * f(b)) < 0:
        b = x_inicial
    if (f(a) * f(x_inicial)) > 0:
        a = x_inicial

    c = b - a
    x_inicial = (a + b) / 2
    contador += 1

    if contador >= limit_itera:
        break


print(
    f"\n\a Raiz:{x_inicial} \n Iterações:{contador} \n valor de f({x_inicial}) = {f(x_inicial)} \n"
)
