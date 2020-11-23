from Calculator.Sqrt import sqrt
from Stats.VarP import variance


def samplestddev(num):
    try:
        variance_float = variance(num)
        return round(sqrt(variance_float), 5)
    except ZeroDivisionError:
        print("Can't Divide by 0 Error")
    except ValueError:
        print("Please Check your data inputs")