#!/usr/bin/env python3

import boto3 
print(boto3)
from pprint import pprint
# print(dir(boto3))
from boto3 import session 
profile_name = 'root'
region_name = 'us-east-2'
service_name = 'ec2'
print(session)
# aws_man_con = boto3.session.Session(profile_name = 'root')
ec2_con_client = boto3.client(service_name = 'ec2',region_name = 'us-east-2')
response = ec2_con_client.describe_instances()

pprint(response['Reservations'])
for each_item in response['Reservations']:
    pprint(each_item['Instances'])
    for each in each_item['Instances']:
        print("========================")
        print(each['ImageId'])
        print("========================")
        print(each['InstanceId'])
        print("========================")
        print(each['LaunchTime'])
        print("========================")
        print(each['Monitoring'])
        print("========================")
        print("enjoy the inventory script for the aws instance")
        print("========================")
        print("The Image Id is: {}\nThe Instance Id Is: {}\nThe Launch Time Is: {}\nThe Monitoring is: {}".format(each['ImageId'],each['InstanceId'],each['Monitoring'],each['LaunchTime'].strftime('%d-%m-%Y')))


