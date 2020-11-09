from Calculator.Division import division


def proportion(num):
    try:
        p_list = list()
        x = sum(num)
        for i in num:
            y = division(i, x)
            p_list.append(y)
        return p_list
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")
