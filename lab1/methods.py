from decimal import Decimal
from answer import Answer
from constants import EPS
from lab1.variant import Variant3 as Var
from math import sqrt

DELTA = EPS / Decimal(2)


def dichotomy(f, a, b):
    x1 = a
    while b - a > EPS:
        m = (a + b) / Decimal(2)
        x1 = m - DELTA
        x2 = m + DELTA
        f1 = f(x1)
        f2 = f(x2)
        if f1 < f2:
            b = x2
        elif f1 > f2:
            a = x1
        else:
            a, b = x1, x2

    return Answer(x1, f(x1))


def fibonacci(f, a, b):
    pass


def fibonacci_n(n):
    return Decimal("1") / Decimal("5").sqrt() * (
            ((Decimal("1") + Decimal("5").sqrt()) / Decimal("2")) ** Decimal(n) -
            ((Decimal("1") - Decimal("5").sqrt()) / Decimal("2")) ** Decimal(n)
    )


def gradient_descent():

    def f(x):
        return (x[1] - x[0]) ** 2 + 100 * (1 - x[0]) ** 2

    def f_x0(x):
        return 202 * x[0] - 2 * x[1] - 200

    def f_x1(x):
        return 2 * x[1] - 2 * x[0]

    eps_f = Decimal(1e-2)
    eps_x = (Decimal(1e-2), Decimal(1e-2))
    X = [Decimal(100), Decimal(100)]
    iterations = 0

    while True:
        iterations += 1
        gradient = [f_x0(X), f_x1(X)]
        gradient_len = Decimal(sqrt(sum(x_i ** 2 for x_i in gradient)))
        S = []
        for x_i in gradient:
            S.append(x_i / gradient_len)

        def g(lam):
            args = [X[i] - lam * S[i] for i in range(len(X))]
            return f(args)

        l = dichotomy(g, Decimal(-200), Decimal(200)).x

        X_next = []
        for i in range(len(X)):
            X_next.append(X[i] - l * S[i])

        flag = True
        for i in range(len(X)):
            if X_next[i] - X[i] > eps_x[i]:
                flag = False
                break

        if abs(f(X_next) - f(X)) < eps_f or flag:
            print(X_next)
            print(f(X_next))
            print(iterations)
            break

        X = X_next
        print(f(X))


def main():
    print(dichotomy(Var.f, Var.a, Var.b))
    print(fibonacci_n(5))


if __name__ == '__main__':
    main()
