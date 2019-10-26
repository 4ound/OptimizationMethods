from decimal import Decimal

from answer import Answer, Segment
from constants import EPS
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


def increase(f, a, b):
    h = 0
    x = []
    k = 0
    x.append(Decimal(1.9))
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


def main():
    print(dichotomy(Var.f, Var.a, Var.b))
    print(fibonacci(Var.f, Var.a, Var.b))
    print(golden_ratio(Var.f, Var.a, Var.b))
    print(increase(Var.f, Var.a, Var.b))


if __name__ == '__main__':
    main()
