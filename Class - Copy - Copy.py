class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

car1 = Car("Audi", "A6", 2020, "Blue")
car2 = Car("Ford", "Mustang", 2022, "Red")

print(car1.make)   
print(car2.speed)  
print(car2.year)
print(car1.year)
print(car1.speed)