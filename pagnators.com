#  This Python code uses the Boto3 library to list all the EC2 instances in an AWS account using a paginator

import boto3

# Create a Boto3 EC2 client

ec2 = boto3.client('ec2')

# Create a paginator for listing EC2 instances

paginator = ec2.get_paginator('describe_instances')

# Iterate over all EC2 instances using the paginator

for page in paginator.paginate():
    for reservation in page['Reservations']:
        for instance in reservation['Instances']:
            # Print the instance ID and state
            print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
            
            
# In this code, we first create a Boto3 EC2 client using the boto3.client() method. We then create a paginator for listing EC2 instances using the get_paginator() method and passing in the name of the describe_instances API action.

# We then iterate over all EC2 instances using the paginator by calling the paginate() method and looping over each page returned. For each page, we then loop over each reservation and each instance within the reservation, and print the instance ID and state using formatted strings.

# This code will print out a list of all the EC2 instances in the account, along with their current state.
            
            
            
