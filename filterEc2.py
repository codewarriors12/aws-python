#!/usr/bin/python3
import boto3
ec2 = boto3.resource('ec2')
state = 'running'
instance = ec2.instances.filter(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [
                            state
                          ]
            }
    ]
)
print (f' instances are "{state}":')
for instance in instance:
    print(f' instance id: {instance.id}')                                         