import math as m

tolerance = 1e-10
initial_value = float(input("Digite o valor inicial: "))
final_value = float(input("Digite o valor de final: "))
limit_it = 4

f = lambda x: x ** 3 - 9 * x + 3
f2 = lambda x: x * x + m.log(x)


def same_sign(a, b):
    return a * b > 0


def bissection(f, initial_value, final_value, tolerance=None):
    # verificando sinal
    assert not same_sign(f(initial_value), f(final_value))
    for i in range(limit_it):
        point_mid = (initial_value + final_value) / 2.0
        if same_sign(f(initial_value), f(point_mid)):
            initial_value = point_mid
        else:
            final_value = point_mid
        if tolerance is not None and abs(final_value - initial_value) < tolerance:
            break
    print(
        f"\n\a Raiz:{point_mid} \n Iterações:{i} \n valor de f({point_mid}) = {f(point_mid)} \n"
    )


bissection(f2, initial_value, final_value, tolerance)
