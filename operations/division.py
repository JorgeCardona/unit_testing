def division(x, y):
    try:
        return x / y
    except ZeroDivisionError as err:
        print('Handling run-time error:', err)
