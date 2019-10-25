from constants import EPS, PRECISION


class Answer:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"F(x) = {round(self.y, PRECISION)}, while x = {round(self.x, PRECISION)}"

    def __eq__(self, other):
        return self.x - EPS <= other.x <= self.x + EPS and self.y - EPS <= other.y <= self.y + EPS
