from Calculator.Square import root
from Stats.VarP import variance


def stddev(num):
    try:
        variance_float = variance(num)
        return round(root(variance_float), 5)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")