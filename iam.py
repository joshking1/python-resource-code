#!/usr/bin/env python3

from time import strftime
import boto3 

from pprint import pprint

aws_man_con = boto3.session.Session(profile_name='root') # logging to management
iam_con_client = aws_man_con.client(service_name='iam',region_name='us-east-2') #logging to resource console
s3_con_client = aws_man_con.client(service_name='s3',region_name='us-east-2') #logging to s3 resource console

# My aim is to list all the users in the aws management console
#response = iam_con_client.list_users()
#pprint(response['Users'])
response = s3_con_client.list_buckets()
print('=========================')
pprint(response['Buckets'])
print('==============================')
for each_bucket in response['Buckets']:
    print(each_bucket['Name']) 
    print(each_bucket['CreationDate'])                      
    print('===============================')
"""
for each_item in response['Roles']:
    print('==========================')
    print(each_item['RoleName'])
    print("===============================")
    print(each_item['RoleId'])
    print('=============================')
    print(each_item['CreateDate'])
    print('=============================')
"""

"""
for each in response['Users']:
    print('==================')
    print(each['UserName'])
    print('===================')
    print(each['UserId'])
    print('====================')
    print(each['CreateDate'])
    print('==================')
"""