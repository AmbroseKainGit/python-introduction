def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannor be 0.")
    return dividend / divisor


#grades = [78, 99, 85, 100]
grades = []
print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print('There are no grades yet in you list')
else:
    print(f"The average grade is {average}")
finally:
    print("Finally")

students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": [50]},
    {"name": "Jen", "grades": [100, 90]}
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}")
except ZeroDivisionError as e:
    print(f'ERROR: {name} has no grades!')
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation")
