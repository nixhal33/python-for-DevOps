import sys,os

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

# example of using environment variables
print(os.getenv("password"))
print(os.getenv("api_token"))

# what i did was first i simply in terminal added : "export password=nixhell" and "export api_token=12345" and then i used the os module to get the values of the environment variables. This output will get an error so also don't forget to use the sys module to pass the arguments in terminal like this: "python3 sys.py 10 add 20" and it will give you the output of 30 and further password and api_token will be printed as well.
