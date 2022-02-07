tolerance = 5e-2


a = float(input("Digite o valor inicial: "))
b = float(input("Digite o valor de final: "))
limit_it = 150

f = lambda x: x ** 3 - 9 * x + 3
# f2 = lambda x: x * x + m.log(x)


def same_sign(a, b):
    return a * b > 0


def bissection(f, a, b, tolerance):
    # verificando sinal
    assert not same_sign(f(a), f(b))
    for i in range(1, limit_it):
        point_mid = (a + b) / 2.0
        if same_sign(f(a), f(point_mid)):
            a = point_mid
        else:
            b = point_mid
        if tolerance is not None and abs(b - a) < tolerance:
            break
    print(
        f"\n\a Raiz:{point_mid} \n Iterações:{i} \n valor de f({point_mid}) = {f(point_mid)} \n"
    )


bissection(f, a, b, tolerance)
