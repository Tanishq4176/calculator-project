# Calculator Project
# Author: Tanishq
# Version 1.0


# calculator.py
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

print("Select operation: 1.Add 2.Subtract 3.Multiply 4.Divide")
choice = int(input("Enter choice: "))
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if choice == 1: print("Result:", add(x, y))
elif choice == 2: print("Result:", subtract(x, y))
elif choice == 3: print("Result:", multiply(x, y))
elif choice == 4: print("Result:", divide(x, y))
else: print("Invalid choice")
