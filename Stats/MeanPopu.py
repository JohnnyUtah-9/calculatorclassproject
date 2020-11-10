from Calculator.Addition import addition
from Calculator.Division import division


def populationmean(num):
    try:
        num_values = len(num)
        total = sum(num)
        return division(total, num_values)
    except ZeroDivisionError:
        print("Error: Cannot Divide by 0")
    except ValueError:
        print("Check your data inputs")