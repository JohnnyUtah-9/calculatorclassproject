from Stats.zScore import zscore


def correlation(data, data1):
    try:
        z1 = zscore(data)
        z2 = zscore(data1)
        z1_z2 = list(map(lambda x, y: x * y, z1, z2))
        corr = sum(z1_z2) / len(z1_z2)
        return round(corr, 7)
    except ZeroDivisionError:
        print("Error: cannot divide by Zero")
    except ValueError:
        print("Please look over your input")
