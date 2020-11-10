from Calculator.Sqrt import root
from Stats.MeanPopu import populationmean
from Stats.sdP import stddev


def confidence_interval_bottom(num):
    try:
        num_values = len(num)
        z = 1.96
        sd = stddev(num)
        avg = populationmean(num)
        return round(avg - (z * sd / root(num_values)), 5)
    except ZeroDivisionError:
        print("Can't Divide by 0 Error")
    except ValueError:
        print("Please Check your data inputs")