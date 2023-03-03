t = 5, 11
x, y = t
print(x, y)

student_attendance = {"Rolf": 94, "Adam": 80, "Anne": 100}
# List of tuples cause items return a list of tuples
print(list(student_attendance.items()))
for key, val in student_attendance.items():
    print(f"{key}: {val}")
for tuple in student_attendance.items():
    print(tuple)
people = [("Bob", 42, "mechanic"), ("James", 24,
                                    "Artist"), ("Harry", 32, "Lecturer")]

for name, age, prof in people:
    print(f"Name: {name}, Age: {age}, Proffesion: {prof}")
for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Proffesion: {person[2]}")

person = ("Bob", 42, "mechanic")
name, _, prof = person
print(name, prof)
# The * means collecting so it will collect all the other values that doesnt match the de estructuring
head, seconde, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)
