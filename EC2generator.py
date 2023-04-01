#!/usr/bin/env python3.11

import random
import string
import secrets

def generateRandomString(length):
    """Generate a random string of fixed length """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


ec2Names = "EC2-"
departments = [ "MARKETING", "ACCOUNTING", "FINOPS" ]


# Allow employee to select their department
department = input("What department do you want to use? ").upper()

if department in departments:
    
    numberOfInstances = input("How many instances do you want to create? ")

    for i in range (int(numberOfInstances)):
        ec2Names = ec2Names + generateRandomString(10)
        print(ec2Names)
        ec2Names = "EC2-"
else:
    print("Invalid department")
    exit()

    


