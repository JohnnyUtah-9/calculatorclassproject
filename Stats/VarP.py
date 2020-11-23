from Calculator.Square import square
from Calculator.Division import division
from Calculator.Square import square
from Stats.MeanPopu import populationmean

def variance(num):
    try:
        pop_mean = populationmean(num)
        num_values = len(num)
        x = 0
        for i in num:
            x = x + square(i - pop_mean)
        return division(x, num_values)
    except ZeroDivisionError:
        print("Can't Divide by 0 Error")
    except ValueError:
        print("Please Check your data inputs")