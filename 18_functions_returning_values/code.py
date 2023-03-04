def add(x, y=8):
    return x + y


sum = add(x=5)
print(sum)


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return 'You Fool!'


result = divide(15, 0)
print(result)