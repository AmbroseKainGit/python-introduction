list = ["bob", "rolf","Anne"]
tuple = ("bob", "rolf","Anne") # Cant modify a tuple
set = {"bob", "rolf","Anne"} # Cant have duplicate elements / Order is not garanted

print(f"LIST {list[0]}")
list[0] = "Guam"
print(f"LIST {list[0]}")
list.append("Cris")
print(list)
list.remove("Guam")
print(list)
set.add("DonGuam")
set.add("DonGuam")
print(set)

