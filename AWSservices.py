#!/usr/bin/env python3.11

"""
Empty List initially to be filled with some of the AWS services
i.e. S3, DynamoDB, EC2, CloudFront, SAM, etc.
"""
ListServices = []

"""
Manually fill our list of services using the .append method followed by print
"""
ListServices.append("S3")
ListServices.append("DynamoDB")
ListServices.append("EC2")
ListServices.append("CloudFront")
ListServices.append("SAM")
ListServices.append("IAM")

print("Contenst of our List: ",ListServices) # Print the list

ListServices.sort() # Sort the list
print("Sorted List: ",ListServices) # Print the sorted list

ListServices.reverse() # Reverse the list
print("Reversed List: ",ListServices) # Print the reversed list

ListServices.remove("S3") # Remove the S3 service from the list
ListServices.remove("DynamoDB") # Remove the DynamoDB service from the list


print("List after removing S3 and DynamoDB: ",ListServices) # Print the list
