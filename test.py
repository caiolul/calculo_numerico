# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Hello world")

# import math as m

# tole = 1e-3
# amplitude = 1e-2
# contador = 0
# a = int(input("Digite o valor de A: "))
# b = int(input("Digite o valor de B: "))
# c = b - a
# limit_itera = 150


# def f(x):
#     f =  x**2 - x - 1
#     return f


# x_inicial = (a + b) / 2


# while c > amplitude or m.fabs(f(x_inicial) > tole):
#     if (f(a) * f(b)) < 0:
#         b = x_inicial
#     if (f(a) * f(x_inicial)) > 0:
#         a = x_inicial

#     c = b - a
#     x_inicial = (a + b) / 2
#     contador += 1

#     if contador >= limit_itera:
#         break


# print(
#     f"\n\a Raiz:{x_inicial} \n Iterações:{contador} \n valor de f({x_inicial}) = {f(x_inicial)} \n"
# )


def bisection(f, a, b, N):
    """Approximate solution of f(x)=0 on interval [a,b] by bisection method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    x_N : number
        The midpoint of the Nth interval computed by the bisection method. The
        initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
        midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iteration, the bisection method fails and return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> bisection(f,1,2,25)
    1.618033990263939
    >>> f = lambda x: (2*x - 1)*(x - 3)
    >>> bisection(f,0,1,10)
    0.5
    """
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1, N + 1):
        m_n = (a_n + b_n) / 2
        f_m_n = f(m_n)
        if f(a_n) * f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n) * f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n) / 2


f = lambda x: x*x*x - x*x + 2 

aproxx = bisection(f, -200, 300, 150)
print(aproxx)
