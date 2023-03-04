from operator import itemgetter


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannor be 0.")
    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)


def search(seq, expected, finder):
    for element in seq:
        if finder(element) == expected:
            return element
    raise RuntimeError(f"Could not find an element with {expected}")


friends = [
    {"name": "Rolf Smith", "age":  24},
    {"name": "adam Smith", "age":  28},
    {"name": "anne Smith", "age":  26},
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Rolf Smith", lambda friend: friend["name"]))
print(search(friends, "Rolf Smith", get_friend_name))
print(search(friends, "Rolf Smith", itemgetter("name")))
