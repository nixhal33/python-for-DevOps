a = 10
b = 20

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def modulo(x, y):
    if y == 0:
        return "Cannot modulo by zero"
    return x % y

print(f"Addition: {add(a, b)}")
print(f"Subtraction: {subtract(a, b)}")
print(f"Multiplication: {multiply(a, b)}")
print(f"Division: {divide(a, b)}")
print(f"Modulo: {modulo(a, b)}")

