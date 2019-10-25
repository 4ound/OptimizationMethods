from decimal import Decimal
from answer import Answer


class Variant3:
    a = Decimal("-2")
    b = Decimal("20")
    answer = Answer(Decimal("2"), Decimal("0"))

    @staticmethod
    def f(x):
        return (x - Decimal("2")) ** Decimal("2")


class Variant7:
    a = Decimal("-10")
    b = Decimal("20")
    answer = Answer(Decimal("-1"), Decimal("-5"))

    @staticmethod
    def f(x):
        return x ** Decimal("2") + Decimal("2") * x - Decimal(4)


class Variant8:
    a = Decimal("0")
    b = Decimal("1")
    answer = Answer(Decimal("0.5774"), Decimal("-0.3849"))

    @staticmethod
    def f(x):
        return x ** Decimal("3") - x
