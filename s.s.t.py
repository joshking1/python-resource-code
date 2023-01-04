#!/usr/bin/env python3

import boto3
from boto3 import session
import sys
print(dir(boto3))
print('==========================')
print(dir(sys))
profile_name = 'root'
service_name = 'ec2'
region_name = 'us-east-2'
aws_mag_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-2")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-2")

#while True:
print("This script performs the following actions on ec2 instance")
print("""
    1. start
    2. stop
    3. terminate
    4. reboot
    5. exit
    """)
What_You_Want_To_Do =int(input("What action would you like to perfom to in your instance?: "))
if What_You_Want_To_Do == 1:
    InstanceId = input("what is the Id for your AWS EC2?: ")
    print("Starting your instance.............")
    ec2_con_cli.start_instances(InstanceIds=[InstanceId])
elif What_You_Want_To_Do == 2:
    InstanceId = input("what is the Id for your AWS EC2?: ")
    print("Stopping your instance.............")
    ec2_con_cli.stop_instances(InstanceIds=[InstanceId])
elif What_You_Want_To_Do == 3:
    InstanceId = input("what is the Id for your AWS EC2?: ")
    print("Terminating your instance.............")
    ec2_con_cli.terminate_instances(InstanceIds=[InstanceId])
elif What_You_Want_To_Do == 4:
    InstanceId = input("what is the Id for your AWS EC2?: ")
    print("Rebooting your instance.............")
    ec2_con_cli.reboot_instances(InstanceIds=[InstanceId])
else:
    print("invalid request that is not supported by the server script")
    sys.exit()


     
