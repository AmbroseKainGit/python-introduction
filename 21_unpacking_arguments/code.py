def multiply(*args):
    print("ARGUMENTOSL: ", args)
    total = 1
    for arg in args:
        total = total * arg
    return total


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid aja"


print(apply(1, 3, 5, 6, 7, operator="*"))
# print(multiply(1, 3, 5, 6, 7))


def add(x, y):
    return x + y


# nums = [3, 5]
# print(add(*nums))
# nums_two = {'x': 15, 'y': 20}
# print(add(**nums_two))
