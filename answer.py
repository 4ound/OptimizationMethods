from constants import EPS, PRECISION


class Answer:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"F(x) = {round(self.y, PRECISION)}, while x = {round(self.x, PRECISION)}"

    def __eq__(self, other):
        return self.x - EPS <= other.x <= self.x + EPS and self.y - EPS <= other.y <= self.y + EPS


class Segment:
    def __init__(self, ans1, ans2):
        self.x = ans1
        self.y = ans2

    def __str__(self):
        return f"F(x1) = {round(self.x.y, PRECISION)}, F(x2) = {round(self.y.y, PRECISION)}, while x1 = {round(self.x.x, PRECISION)}, x2 = {round(self.y.x, PRECISION)}"

    def compare(self, other):
        return (self.x.x <= other.x <= self.y.x or self.x.x >= other.x >= self.y.x) and self.x.y >= other.y <= self.y.y
