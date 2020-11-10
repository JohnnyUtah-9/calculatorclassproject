from collections import Counter


def mode(num):
    try:
        num_values = len(num)
        count = Counter(num)
        get_mode = dict(count)
        mode = [k for k, v in get_mode.items() if v == max(list(count.values()))]
        if len(mode) == num_values:
            get_mode = "No mode found"
        else:
            get_mode = mode[0]
        return get_mode
    except ZeroDivisionError:
        print("Divide by 0 Error")
    except ValueError:
        print("Please Check your data inputs")