class student:
    def __init__(self, name, roll_no):  
        self.name = name               
        self.roll_no = roll_no
        print("Inside Constructor:")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
    def update_marks(self, marks):     
        self.marks = marks
        print("\nInside Instance Method:")
        print(f"{self.name}'s Marks Updated to:", self.marks)
s1 = student("Kalyan", 101)
s1.update_marks(95)
