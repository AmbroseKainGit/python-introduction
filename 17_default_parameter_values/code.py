def add(x, y=8):
    result = x + y
    print(result)


add(x=5)

default_y = 3

def add_two(x, y=default_y):
    result = x + y
    print(result)


add_two(x=5)
#Not changing the value in the function cause its already created
default_y = 4
add_two(x=5)