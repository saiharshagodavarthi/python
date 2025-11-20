def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 3 is:", factorial(3))
print("Factorial of 5 is:", factorial(5))