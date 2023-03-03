name = "bob"
greeting = f"Hello, {name}" #F STRING IN PYTHON WHICH ALLOW ENBED STRING IN PY

print(greeting)

name = "Rolf"

print(greeting)
print(f"Hello, {name}")

# TEMPLATE STRING

name2 = "Pokkezan"
greeting2 = "Hello, {}"
with_name = greeting2.format(name2)
print(with_name)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Cristian", "Friday")

print(formatted)

