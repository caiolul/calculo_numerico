def comparison(x, xk, eps):
    soma = 0
    zip_object = zip(x, xk)
    for list1, list2 in zip_object:
        soma = soma + abs(list1 - list2)

    if soma < eps:
        return True
    else:
        return False


def has_soluction(a_array, b_array, x, n):
    result: bool
    for i in list(range(1, n + 1, 1)):
        if abs(a_array[i - 1][i - 1]) > 0.0:
            x[i - 1] = b_array[i - 1] / a_array[i - 1][i - 1]
            result = True
        else:
            result = False
            break
    return result


def jacobi(A, b, it, tol):
    n = len(b)
    x = b.copy()
    print("Metodo de jacobi")
    print("----------------------")
    print("Valor de A:", A)
    print("Valor de b:", b)
    print("Valor de tol:", tol)
    print("----------------------")
    if has_soluction(A, b, x, n):
        print("Iter 0")
        print("x = ", x)
        xk = x.copy()
        iter = 0
        while iter < it:
            iter = iter + 1
            for i in list(range(1, n + 1, 1)):
                su = 0
                for j in list(range(1, n + 1, 1)):
                    if (i - 1) != (j - 1):
                        su = su + A[i - 1][j - 1] * x[j - 1]

                xk[i - 1] = (1 / A[i - 1][i - 1]) * (b[i - 1] - su)

            print("Iter: ", iter)
            print("xk = ", xk)
            if comparison(x, xk, tol):
                x = xk.copy()
                break
            x = xk.copy()
    print("---------Resultado final---------")
    print("x = ", x)
    return x


A = [[10, 2, 1], [1, 5, 1], [2, 3, 10]]

b = [7, -8, 6]

jacobi(A, b, 10, 0.05)
