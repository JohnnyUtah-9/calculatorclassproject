from Calculator.SquareRoot import root
from Statistics.Variance import variance


def samplestddev(num):
    try:
        variance_float = variance(num)
        return round(root(variance_float), 5)
    except ZeroDivisionError:
        print("Can't Divide by 0 Error")
    except ValueError:
        print("Please Check your data inputs")