from Stats.Proportional import proportion
from Stats.VarP import variance


def variance_of_population_proportion(num):
    variance_p = proportion(num)
    return variance(variance_p)