a = 10
b = 20

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulo(a, b):
    if b == 0:
        return "Cannot modulo by zero"
    return a % b

print(f"Addition: {add(a, b)}")
print(f"Subtraction: {subtract(a, b)}")
print(f"Multiplication: {multiply(a, b)}")
print(f"Division: {divide(a, b)}")
print(f"Modulo: {modulo(a, b)}")