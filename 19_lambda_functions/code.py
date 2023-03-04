def add(x, y):
    return x + y


sum = add(5, 7)
print(sum)

print((lambda x, y: x + y)(9, 8))


def double(x):
    return x * 2


sequence = [1, 3, 4, 8]
doubled = [x * 2 for x in sequence]
doubled_two = [double(x) for x in sequence]
doubled_three = map(double, sequence)
doubled_four = [(lambda x: x * 2)(x) for x in sequence]
doubled_five = list(map(lambda x: x * 2, sequence))
