name = input("Enter you name: ")
print(name)
# Input always return a string
size_input = input("How bi is your house: ")
square_feet = int(size_input)
square_metres = square_feet / 10.8
print(f"The number of square meters is: {square_metres:.2f}") # :.2f syntax to return only 2 decimal points
