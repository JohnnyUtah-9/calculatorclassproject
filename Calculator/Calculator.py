from Calculator.Subtraction import subtraction
from Calculator.Addition import addition


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
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

