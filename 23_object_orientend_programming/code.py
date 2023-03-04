student_two = {"name": "Luis", "grades": (89, 80, 93, 79, 90)}

def average_two(sequence):
    return sum(sequence) / len(sequence)

print(average_two(student_two['grades']))


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades) 
        
student = Student("Guamo", (89, 80, 93, 79, 90))
print(student.name)        
print(student.average())        
