import sys

a=10
a+=5
a-=4
print(a)

x = 10
y = 40

result = x & y
print(result)

c = 10 
d = 50
if c == d:
    print("c is equal to d infact it's not equal to d")

type = sys.argv[1]
if type == "t2.micro":
    print("Yes! You can launch t2.micro.")
else:
    print("Sorry, It's not avaiable for you as You need to request for the service quota to the aws...!!!!")
