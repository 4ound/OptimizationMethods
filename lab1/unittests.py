import unittest
from lab1 import variant as var
from lab1.methods import dichotomy


class TestDichotomyMethod(unittest.TestCase):
    def test_3d_variant(self):
        a = var.Variant3.a
        b = var.Variant3.b
        f = var.Variant3.f
        answer = var.Variant3.answer
        self.assertTrue(dichotomy(f, a, b) == answer)

    def test_7th_variant(self):
        a = var.Variant7.a
        b = var.Variant7.b
        f = var.Variant7.f
        answer = var.Variant7.answer
        self.assertTrue(dichotomy(f, a, b) == answer)

    def test_8th_variant(self):
        a = var.Variant8.a
        b = var.Variant8.b
        f = var.Variant8.f
        answer = var.Variant8.answer
        self.assertTrue(dichotomy(f, a, b) == answer)
