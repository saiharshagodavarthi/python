class Student:
    def __init__(self, rno, marks, name, grade):
        self.rno = rno
        self.marks = marks
        self.name = name
        self.grade = grade

std1 = Student(22, 50, "Kalyan", "A")
std2 = Student(25, 40, "Sai", "B")

print(std1.rno)
print(std2.rno)
print(std1.name)
print(std2.name)