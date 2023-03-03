number = 7

# while True:
#     user_input = input("would you like to play? (Y/n) ").lower()
#     if user_input == "n":
#         break
#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print('YOU WIN')
#     elif abs(number - user_number) == 1:
#         print('You were off by one.')
#     else:
#         print('YOU LOSE ')

friends = ["Rolf", "jen", "Bob", "Anne"]
for item in friends:
    print(f"{item} is my friend")

for item in range(4):
    print(f"{item} is my friend")

grades = [35, 67, 98, 100, 100]
total = 0
total_two = sum(grades)
amount = len(grades)

for grade in grades:
    total += grade
print(total / amount)    
print(total_two / amount)    
