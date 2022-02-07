tolerance = 5e-10
a = float(input("Digite o valor inicial: "))
b = float(input("Digite o valor de final: "))
limit_it = 150

f = lambda x: x ** 3 - 9 * x + 3
# f2 = lambda x: x * x + m.log(x)


def same_sign(a, b):
    return a - b != 0


def secant(f, a, b, tolerance=None):
    for i in range(1, limit_it):
        if same_sign(f(a), f(b)):
            x_final = (b * f(a) - a * f(b)) / (f(a) - f(b))
            a = b
            b = x_final

        if tolerance is not None and abs(f(x_final)) < tolerance:
            break
    print(
        f"\n\a Raiz:{x_final} \n Iterações:{i} \n valor de f({x_final}) = {f(x_final)} \n"
    )


secant(f, a, b, tolerance)
