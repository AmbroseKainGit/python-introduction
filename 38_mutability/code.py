from typing import List, Optional
a = []

b = a

print(id(a))
print(id(b))

# Tuples string integers and some others are inmutable in py


class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None) -> None:
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(98)
print(bob.grades)
print(rolf.grades)
