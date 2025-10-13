program-1
--------
syntax
# variable_name = input("message") 
# result = operand1 operator operand2 
# print(result)

program:
-----

kilo_grams = float(input('Enter weight in Kg to Convert into pounds:')) 
pounds = kilo_grams * 2.2 
print(kilo_grams,' Kilograms =', pounds,' Pounds')


------------------------------------------------------------------------------------------------------------

program-2
-------- 
Syntax: 
# for variable in range(start, stop, step): 
#     print(variable) 
 
Program: 
for i in range(8,90,3): 
    print(i,end=" ") 

------------------------------------------------------------------------------------------------------------

progarm-3
--------

Syntax: 
# list_name = list(string_variable) 
 
Program:
text = "Hello" 
char_list = list(text) 
print(char_list)  # Output: ['H', 'e', 'l', 'l', 'o']

------------------------------------------------------------------------------------------------------------

program-4
---------

Syntax: 
# largest = max(list_name) 
# print(largest) 
 
Program: 
numbers = [10, 45, 2, 99, 65] 
largest = max(numbers) 
print("Largest number is:", largest)

----------------------------------------------------------------------------------------------------------

progarm-5
--------


Syntax: 
# def function_name(parameters): 
    # code 
 
Program: 
def fibonacci(n): 
    if n <= 0: 
        return "Invalid input" 
    elif n == 1: 
        return 0 
    elif n == 2: 
        return 1 
    else: 
        return fibonacci(n-1) + fibonacci(n-2) 
n = 7 
print(f"Fibonacci number at position {n} is:", fibonacci(n)) 
