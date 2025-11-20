class Student:
    def __init__(self, x, y, z):
        self.name = x
        self.rollno = y
        self.marks = z
    def display(self):
        print("Student name: {}\nRollno: {}\nMarks: {}".format(self.name, self.rollno, self.marks))
s1 = Student("Kalyan", 101, 50)
s1.display()
s2 = Student("Sunny", 102, 100)
s2.display()
s3 = Student("Raju", 103, 150)
s3.display()
s4= Student("Ravi",104,200)
s4.display()
