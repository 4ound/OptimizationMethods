from decimal import Decimal
from answer import Answer
from constants import EPS, PRECISION
from lab1.variant import Variant3 as Var
from math import sqrt

DELTA = EPS / Decimal(4)


def dichotomy(f, a, b):
    x1 = a
    while abs(b - a) > EPS:
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


def increase(f, lam):
    h = 0
    x = []
    k = 0
    x.append(Decimal(lam))
    if f(x[k]) > f(x[k] + EPS):
        x.append(x[k] + EPS)
        k += 1
        h = EPS
    elif f(x[k]) > f(x[k] - EPS):
        x.append(x[k] - EPS)
        k += 1
        h = -EPS
    h *= 2
    x.append(x[k] + h)
    while f(x[k]) > f(x[k + 1]):
        k += 1
        h *= 2
        x.append(x[k] + h)
    return x[k - 1], x[k + 1]


def gradient_descent():

    def f(x):
        return (x[1] - x[0]) ** 2 + 100 * (1 - x[0]) ** 2

    def f_x0(x):
        answer1 = 202 * x[0] - 2 * x[1] - 200
        args = x[0] + eps_x[0] / 8, x[1]
        answer2 = (f(args) - f(x)) / (eps_x[0] / 8)
        return answer1

    def f_x1(x):
        answer1 = 2 * x[1] - 2 * x[0]
        args = x[0], x[1] + eps_x[1] / 8
        answer2 = (f(args) - f(x)) / (eps_x[1] / 8)
        return answer1

    eps_f = Decimal(10 ** (-PRECISION))
    eps_x = (Decimal(10 ** (-PRECISION)), Decimal(10 ** (-PRECISION)))
    X = [Decimal(0.99), Decimal(0.99)]
    iterations = 0
    calculations = 0

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

        left, right = increase(g, 1)
        if left > right:
            left, right = right, left

        dichotomy_result = dichotomy(g, left, right)
        l = dichotomy_result[0].x

        X_next = []
        for i in range(len(X)):
            X_next.append(X[i] - l * S[i])

        flag = True
        for i in range(len(X)):
            if abs(X_next[i] - X[i]) > eps_x[i]:
                flag = False
                break

        if abs(f(X_next) - f(X)) < eps_f or flag:
            # X_next = [round(X_next[0], PRECISION), round(X_next[1], PRECISION)]

            X_answer = (float(round(X_next[0])), float(round(X_next[1], PRECISION)))
            # print(iterations, calculations, X_answer, round(f(X_next), PRECISION))

            print('1e-' + str(PRECISION), '\t', iterations, '\t', X_answer, '\t',round(f(X_next), PRECISION))

            # print(iterations, )
            # print(calculations, '\t')
            # print(X_answer, '\t')
            # print(round(f(X_next), PRECISION), '\t')

            # print('x_min =', X_next)
            # print('f_min =', round(f(X_next), PRECISION))
            # print(iterations, 'iterations')
            # print(calculations, 'calculations')
            break

        X = X_next
        # print(f(X))


def main():
    # print(dichotomy(Var.f, Var.a, Var.b))
    # print(fibonacci_n(5))
    gradient_descent()


if __name__ == '__main__':
    main()
