import sys

type = sys.argv[1]

if type == "t2.micro":
    print("It will charge you $2 per day")
elif type == "t3.medium":
    print("It will charge you $4 per day")
elif type == "t4.xlarge":
    print("It will charge you $8 per day")
elif type == "g6.xlarge":
    print(f"Try to deploy your gpu based cancer chatbot app using this ec2 instance:'{type}' as it seems to have 4cpu and 16gb ram and plus 1hr equals almost $1 so do fast deployment for this application.")
elif type == "g6.24xlarge":
    print("It's out of your current service quota. Ask for more quota to aws.")
else:
    print("Please Provide a valid instance type")
    