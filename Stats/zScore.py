from Stats.MeanPopu import populationmean
from Stats.sdP import stddev


def zscore(num):
    zmean = populationmean(num)
    sd = stddev(num)
    zlist = []
    for x in num:
        z = round(((x - zmean) / sd), 6)
        zlist.append(z)
    return zlist
