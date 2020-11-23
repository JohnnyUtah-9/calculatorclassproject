from Calculator.Division import division


def samplemean(num):
    try:
        num_values = len(num)
        total = sum(num)
        return round(division(total, num_values), 8)
    except ZeroDivisionError:
        print("Divide by 0 Error")
    except ValueError:
        print("Please Check your data inputs")
