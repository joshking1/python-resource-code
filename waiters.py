# This Python code uses Boto3 waiters to wait for an Amazon Elastic Compute Cloud (Amazon EC2) instance to reach a running state

import boto3

# Create a Boto3 EC2 client
ec2 = boto3.client('ec2')

# Launch an EC2 instance
response = ec2.run_instances(
    ImageId='ami-0c55b159cbfafe1f0',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
)

# Get the instance ID of the launched instance
instance_id = response['Instances'][0]['InstanceId']
print(f"Instance ID: {instance_id}")

# Create a waiter for the instance running state
waiter = ec2.get_waiter('instance_running')

# Wait for the instance to reach the running state
waiter.wait(InstanceIds=[instance_id])

# Get the public IP address of the instance
response = ec2.describe_instances(InstanceIds=[instance_id])
public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
print(f"Public IP address: {public_ip}")


# In this code, we first create a Boto3 EC2 client using the boto3.client() method. 

# We then launch an EC2 instance using the run_instances() method and passing in the required parameters such as the AMI ID, instance type, and minimum and maximum count.

# We then retrieve the instance ID of the launched instance from the response and create a waiter for the instance running state using the get_waiter() method. 

# We pass in the name of the waiter, which is instance_running in this case.

# We then call the wait() method on the waiter and pass in the instance ID of the launched instance using the InstanceIds parameter. 

# This method will wait until the instance reaches the running state before continuing with the next line of code.

# Finally, we retrieve the public IP address of the instance using the describe_instances() method and print it out. This code will wait for the instance to reach the running state before retrieving the public IP address.
