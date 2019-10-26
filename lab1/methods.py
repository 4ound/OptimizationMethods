from decimal import Decimal
from answer import Answer, Segment
from constants import EPS, PRECISION
from lab1.variant import Variant3 as Var
from math import sqrt, fabs

DELTA = EPS / Decimal(4)


def dichotomy(f, a, b):
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

    return Answer(a, f(a))


def fibonacci(f, a, b):
    n = 0
    for i in range(0, 100):
        if (b - a) / EPS < fibonacci_n(i):
            n = i
            break

    la = a + fibonacci_n(n - 2) / fibonacci_n(n) * (b - a)
    mu = a + fibonacci_n(n - 1) / fibonacci_n(n) * (b - a)
    f_la = f(la)
    f_mu = f(mu)
    for k in range(1, n - 1):
        if f_la > f_mu:
            a = la
            la = mu
            f_la = f_mu
            mu = a + fibonacci_n(n - k - 1) / fibonacci_n(n - k) * (b - a)
            f_mu = f(mu)
        else:
            b = mu
            mu = la
            f_mu = f_la
            la = a + fibonacci_n(n - k - 2) / fibonacci_n(n - k) * (b - a)
            f_la = f(la)

    mu = la + EPS
    f_mu = f(mu)
    if f_la < f_mu:
        b = mu
    else:
        a = la

    x = (b + a) / Decimal("2")
    return Answer(x, f(x))


def fibonacci_n(n):
    return Decimal("1") / Decimal("5").sqrt() * (
            ((Decimal("1") + Decimal("5").sqrt()) / Decimal("2")) ** Decimal(n) -
            ((Decimal("1") - Decimal("5").sqrt()) / Decimal("2")) ** Decimal(n)
    )


def golden_ratio(f, a, b):
    t = Decimal((sqrt(5) - 1) / 2)
    x1 = Decimal(a + (1 - t) * (b - a))
    x2 = Decimal(a + t * (b - a))
    f1 = f(x1)
    f2 = f(x2)
    while fabs(b - a) > EPS:
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + t * (b - a)
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            x1 = a + (1 - t) * (b - a)
            f2 = f1
            f1 = f(x1)
    x = (a + b) / 2
    return Answer(x, f(x))


def increase(f, a=0, b=0, lam=1.9):
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
    ans1 = Answer(x[k - 1], f(x[k - 1]))
    ans2 = Answer(x[k + 1], f(x[k + 1]))
    return Segment(ans1, ans2)


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

        answer = increase(g, 1)
        left, right = answer.x.x, answer.y.x
        if left > right:
            left, right = right, left

        dichotomy_result = dichotomy(g, left, right)
        l = dichotomy_result.x

        X_next = []
        for i in range(len(X)):
            X_next.append(X[i] - l * S[i])

        flag = True
        for i in range(len(X)):
            if abs(X_next[i] - X[i]) > eps_x[i]:
                flag = False
                break

        if abs(f(X_next) - f(X)) < eps_f or flag:
            X_answer = (float(round(X_next[0])), float(round(X_next[1], PRECISION)))
            return '1e-' + str(PRECISION), '\t', iterations, '\t', X_answer, '\t',round(f(X_next), PRECISION)

        X = X_next


def main():
    print(dichotomy(Var.f, Var.a, Var.b))
    print(fibonacci(Var.f, Var.a, Var.b))
    print(golden_ratio(Var.f, Var.a, Var.b))
    print(increase(Var.f, Var.a, Var.b))
    print(gradient_descent())


if __name__ == '__main__':
    main()
