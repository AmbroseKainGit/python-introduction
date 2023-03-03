numbers = [1, 3, 5]
doubled = [num * 2 for num in numbers] # Thing that i want in the new list then the for loop
print(doubled)
friends = ["Rolf", "Sam", "Samantha"]
friends_two = [friend for friend in friends if friend.startswith("S")]
print(friends_two)
print("Friends: ", id(friends), "friends_two", id(friends_two)) # Id = to the memory address