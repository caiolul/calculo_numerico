def factorization_lu(A):
    n = len(A)
    print("------------")
    print("Matriz A:", A)
    print("------------")
    new_array = A.copy()
    for k in list(range(1, n, 1)):
        for i in list(range(k + 1, n + 1, 1)):
            # pivoteamento
            if abs(A[k - i][k - 1]) > abs(A[k - 1][k - 1]):
                new_array[k - 1] = A[k - i]
                new_array[k - i] = A[k - 1]
            A = new_array.copy()
            m = A[i - 1][k - 1] / A[k - 1][k - 1]
            A[i - 1][k - 1] = m
            for j in list(range(k + 1, n + 1, 1)):
                A[i - 1][j - 1] = A[i - 1][j - 1] - m * A[k - 1][j - 1]
        print("------------")
        print("Matriz LU:", A)
        print("------------")
        return A


def lower_triangular(L, b):
    n = len(b)
    y = [0] * n
    for i in list(range(1, n + 1, 1)):
        s = 0
        for j in list(range(1, i, 1)):
            s = s + L[i - 1][j - 1] * y[j - 1]

        y[i - 1] = b[i - 1] - s
    print("------------")
    print("Matriz L:", y)
    print("------------")
    return y


def upper_triangular(U, b):
    n = len(b)
    x = [0] * n
    x[n - 1] = b[n - 1] / U[n - 1][n - 1]
    for i in list(range(n - 1, 0, -1)):
        s = 0
        for j in list(range(i + 1, n + 1, 1)):
            s = s + U[i - 1][j - 1] * x[j - 1]

        x[i - 1] = (b[i - 1] - s) / (U[i - 1][i - 1])
    print("------------")
    print("Matriz U:", x)
    print("------------")
    return x


Ai = [[3, 2, 4], [1, 1, 2], [4, 3, -2]]
Ai2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
bi = [1, 2, 3]

A = factorization_lu(Ai2)
y = lower_triangular(A, bi)
x = upper_triangular(A, y)
