import math as m

tolerance = 1e-10
initial_value = float(input("Digite o valor inicial: "))
final_value = float(input("Digite o valor de final: "))
limit_it = 150

f = lambda x: x ** 3 - 9 * x + 3
f2 = lambda x: x * x + m.log(x)


def same_sign(a, b):
    return a * b > 0


def secant(f, initial_value, final_value, tolerance=None):
    assert not same_sign(f(initial_value), f(final_value))
    for i in range(1, limit_it):
        if (f(initial_value) - f(final_value)) != 0:
            x_final = (
                initial_value * f(final_value) - final_value * f(initial_value)
            ) / (f(final_value) - f(initial_value))
            initial_value = final_value
            final_value = x_final

        if tolerance is not None and abs(f(x_final)) < tolerance:
            break
    print(
        f"\n\a Raiz:{x_final} \n Iterações:{i} \n valor de f({x_final}) = {f(x_final)} \n"
    )


secant(f, initial_value, final_value, tolerance)
