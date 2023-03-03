# Asocieate keys and values togheter
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 28}
friend_ages["Adam"] = 50
friend_ages["Bob"] = 26
print(friend_ages)

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 23},
    {"name": "Bob", "age": 27},
    {"name": "Anne", "age": 30},
]
print(friends[0]["name"])
attendances = {"Rolf": 94, "Adam": 80, "Anne": 100}
for key, val in attendances.items():
    print(f"{key}: {val}")

if "Bob" in attendances:
    print("IN")
else:
    print("OUT")    
    
    
values = attendances.values()
print(sum(values) / len(values))