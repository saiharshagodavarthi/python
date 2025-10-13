progarm-1
--------

# Syntax: 
# class ClassName: 
#     def __init__(self, attr1, attr2): 
#         self.attr1 = attr 
#     def method_name(self): 
        # code 
 
Program: 
class Car: 
    def _init_(self, make, model, year): 
        self.make = make 
        self.model = model 
        self.year = year 
        self.is_started = False 
    def start(self): 
        if not self.is_started: 
          self.is_started = True 
            print(f"The {self.year} {self.make} {self.model} is starting.") 
        else: 
            print(f"The {self.year} {self.make} {self.model} is already running.") 
    def stop(self): 
        if self.is_started: 
            self.is_started = False 
            print(f"The {self.year} {self.make} {self.model} is stopping.") 
        else: 
            print(f"The {self.year} {self.make} {self.model} is already stopped.") 
# Create a car object 
print("---car class demonstration") 
my_car = Car("Toyota", "Camry", 2022) 
print(f"my car:{my_car.make} {my_car.model} ({my_car.year})") 
# Start and stop the car 
my_car.start() 
my_car.stop() 
my_car.start() 
my_car.stop() 

------------------------------------------------------------------------------------------------------

progarm-2
--------

Syntax: 
# class BaseClass: 
    # base class code 
# class DerivedClass(BaseClass): 
    # derived class code 
 
Program: 
# Base Class - Animal 
class Animal: 
    def __init__(self, name): 
        self.name = name 
    def speak(self): 
        return "Some generic animal sound" 
    def move(self): 
        return "The animal moves around" 
# Derived Class - cat 
class cat(Animal): 
    def speak(self):
       return f"{self.name} says: Meow! Meow!" 
    def move(self): 
        return f"{self.name} runs quietly." 
# Demonstration 
cat = cat("cutie") 
animals = [cat] 
for animal in animals: 
    print(animal.speak()) 
    print(animal.move()) 

--------------------------------------------------------------------------------------------------

progarm-3
---------

Syntax: 
# class Base: 
    # def method(self): 
        # base code 
# class Derived(Base): 
    # def method(self): 
        # overridden cod 
 
Program: 
class Animal: 
    def make_sound(self): 
        raise NotImplementedError("Subclass must implement abstract method 'make_sound'") 
class Dog(Animal): 
    def make_sound(self): 
        return "Woof! Woof!" 
class Cat(Animal): 
   def make_sound(self): 
        return "Meow!" 
class Bird(Animal): 
    def make_sound(self): 
        return "Chirp! Chirp!" 
# Demonstrating polymorphism 
print("\n--- Polymorphism Demonstration ---") 
animals = [Dog(), Cat(), Bird()] 
for animal in animals: 
    print(f"An animal makes sound: {animal.make_sound()}") 

-----------------------------------------------------------------------------------------------------
program-4
---------

Syntax: 
try: 
    # code that may raise exception 
except ExceptionType: 
    # code to handle exception 
 
Program: 
def safe_divide(numerator, denominator): 
    try: 
        result = numerator / denominator 
        print(f"The result of {numerator} / {denominator} is: {result}") 
    except ZeroDivisionError: 
        print(f"Error: Cannot divide by zero! Attempted {numerator} / {denominator}") 
    except TypeError: 
        print("Error: Invalid input types. Please provide numbers.") 
    except Exception as e: 
        print(f"An unexpected error occurred: {e}") 
# Demonstrating error handling 
print("\n--- Error Handling Demonstration ---") 
safe_divide(10, 2) 
safe_divide(10, 0) 
safe_divide(5, "abc")

-----------------------------------------------------------------------------------------------------









