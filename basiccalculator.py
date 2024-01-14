// this is a basic calculator using python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
print("1. Addition:", add(num1, num2))
print("2. Subtraction:", subtract(num1, num2))
print("3. Multiplication:", multiply(num1, num2))
print("4. Division:", divide(num1, num2))

