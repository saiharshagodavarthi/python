class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print('Hi', self.name)
        print('Your marks are:', self.marks)

    def grade(self):
        if self.marks >= 60:
            print('You got First Grade')
        elif self.marks >= 50:
            print('You got Second Grade')
        elif self.marks >= 35:
            print('You got Third Grade')
        else:
            print('You are Failed')
n = int(input('Enter number of students: '))
for i in range(n):
    name = input('Enter Name: ')
    marks = int(input('Enter Marks: '))
    s = Student(name, marks)
    s.display()
    s.grade()
    print()