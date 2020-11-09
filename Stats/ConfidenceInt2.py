from Calculator.SquareRoot import root
from Statistics.PopulationMean import populationmean
from Statistics.StandardDeviation import stddev


def confidence_interval_top(num):
    try:
        num_values = len(num)
        z = 1.96
        sd = stddev(num)
        avg = populationmean(num)
        return round(avg + (z * sd / root(num_values)), 5)
    except ZeroDivisionError:
        print("Can't Divide by 0 Error")
    except ValueError:
        print("Please Check your data inputs")