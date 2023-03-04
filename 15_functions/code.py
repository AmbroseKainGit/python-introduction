def hello():
    print("hello")


hello()


def user_age_in_seconds():
    user_age = int(input("Enter you age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")


user_age_in_seconds()


def add_friend():
    friends.append("Rolf")


friends = []
add_friend()

print(friends)
