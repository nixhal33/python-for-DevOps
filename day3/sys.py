import sys

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

a = int(sys.argv[1])
operation = sys.argv[2]
b = int(sys.argv[3])

if operation == "add":
    output = add(a, b)
    print(output)
elif operation == "subtract":
    output = subtract(a, b)
    print(output)
elif operation == "multiply":
    output = multiply(a, b)
    print(output)
elif operation == "divide":
    output = divide(a, b)
    print(output)
elif operation == "modulo":
    output = modulo(a, b)
    print(output)