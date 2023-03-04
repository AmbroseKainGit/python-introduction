def named(name, age):
    print(name, age)  # Prints a Dictionary {} with the key value pairs


def named_two(**kwargs):
    print(kwargs)  # Prints a Dictionary {} with the key value pairs


details = {"name": "Bob", "age": 25}
# named(**details)
# named_two(**details)


def print_nicely(**kwargs):
    named_two(**kwargs)
    for arg, values in kwargs.items():
        print(f"{arg}: {values}")


print_nicely(name="Bob", age=25)


def both(*args, **kwargs):
    print(args)
    print(kwargs)
    
both(1,3,5, name="bjhon", age=30)    


def myfunction(**kwargs):
    print(kwargs)
    
myfunction(**"Bob") #Error must be mapping    