#!/usr/bin/python3
import boto3
import os

print("printing all ec2")
print("_______________________________________")
print()

ec2 = boto3.resource('ec2', region_name= 'us-east-1')
instance = ec2.instances.all()
for instance in instance:
        print (f' ec2 instance "{instance.id}:')
        print (f' instance state: {instance.state["Name"]}')
        print (f' public ip address: {instance.public_ip_address}')
    print("____________________________________________")
    print()
