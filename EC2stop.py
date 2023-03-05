#!/usr/bin/python3
import boto3
import json

ec2 = boto3.client('ec2')
tag = input("Enter tag value of EC2 to stop: ")
print()
state = 'running'
if tag == 'instance_devenv':
    running_instances = ec2.describe_instances(Filters=[{
        'Name': 'instance-state-name',
        'Values': ['running'],
        'Name': 'tag:Name',
        'Values': ['instance_devenv']}])
    print (f' instances are "{state}" :')
    print("---------------------------------------------------------------------")
    print("filtering and counting only running instances with specific tag")

    for value in running_instances:
        filters = [{'Name': 'tag:Name', 'Values': ['instance_devenv']}]
        instances = ec2.describe_instances(Filters=filters)
        #json_string = json.dumps(instances, indent=2, default=str)
        #print(json_string)

        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                public_ip = instance['PublicIpAddress']
                print(f' instance is : {instance_id},{public_ip}')
                ec2.stop_instances(InstanceIds=[instance_id])
            print("------------------------------------------------------------------")
            print("stopping only running instances with provided tag")
    print("instances has been stopped")