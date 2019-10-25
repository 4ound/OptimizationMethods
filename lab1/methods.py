from decimal import Decimal
from answer import Answer
from constants import EPS
from lab1.variant import Variant3 as Var

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


if __name__ == '__main__':
    print(dichotomy(Var.f, Var.a, Var.b))
