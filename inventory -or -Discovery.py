#!/usr/bin/env python3

import boto3 
from boto3 import session
profile_name = "root"
region_name = 'us-east-2'
service_name = 'ec2'
from pprint import pprint
aws_ec2_con = boto3.client(service_name="ec2",region_name='us-east-2')
response=aws_ec2_con.describe_instances()
pprint(response['Reservations'])
for each_item in response['Reservations']:
    pprint(each_item['Instances'])
    for each in each_item['Instances']:
        pprint("=============================")
        print(each['ImageId'])
        pprint("=============================")
        print(each['VirtualizationType'])
        pprint("=============================")
        print(each['SubnetId'])
        pprint("=============================")
        print("The Image Id is: {}\nThe Instance Id Is: {}\nThe Instance Launch Time is: {}".format(each['ImageId'],each['InstanceId'],each['LaunchTime'].strftime("%d-%m-%Y")))

        #print(each_item['Instances'])
response = aws_ec2_con.describe_volumes()
print("==========================")
print(response['Volumes'])
for each_item in response['Volumes']:
    print("==========================")
    pprint(each_item['State'])
    print("==========================")
    pprint(each_item['VolumeId'])
    print("==========================")
    print("The Create Time is: {}\nThe Volume Id is: {}\nThe State is: {}".format(each_item['CreateTime'],each_item['VolumeId'],each_item['State']))
    
    #for each in each_item['VolumeId']:
        #print(each)



#'State'
    #'Instances'
    