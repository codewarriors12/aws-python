#!/usr/bin/env python
# Create a list of services using Python - S3, EC2, DynamoDB, Lambda, Cloudwatch
awssvclist = []
print(f'current aws svc list {awssvclist}')

# Populate the list using append or insert.
awssvclist.insert(0,'S3')
awssvclist.insert(1,'EC2')
awssvclist.insert(2,'Dynamodb')
awssvclist.insert(3,'Lambda')
awssvclist.append('CloudWatch')

# Print the list and the length of the list.
print("The length of the aws svc list is - ", len(awssvclist))
print(awssvclist)

# Remove two specific services from the list by name or by index.
del awssvclist[2:4]

# Print the new list and the new length of the list.
print(f'The new length of the aws svc list is {len(awssvclist)}')
print(awssvclist)
