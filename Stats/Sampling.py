from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Calculator.Divison import divison
from Calculator.multiplication import multiplication
from Calculator.Sqrt import Sqrt
from Calculator.Square import Square
from random import random

class Sample:
    result = 0

    def __init__(self):
        pass

    def randimize(self, p, k):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = Subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = Divison(a, b)
        return self.result

    def sqr(self, a):
        self.result = Square(a)
        return self.result

    def sqrt(self, a, b):
        self.result = Sqrt(a, b)
        return self.result

