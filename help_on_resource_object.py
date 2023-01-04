#!/usr/bin/env python3

import boto3

aws_mag_con=boto3.session.Session(profile_name="root")
'''
iam_con_re=aws_mag_con.resource(service_name="iam",region_name="us-east-1")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
'''
s3_con_re=aws_mag_con.resource(service_name="s3",region_name="us-east-2")

'''
#List all iam users 
for each_item in iam_con_re.users.all():
	print(each_item.user_name)
'''

for each_item in s3_con_re.buckets.all():
	print(dir(each_item))

	print(each_item.name)
	print(each_item.objects)
	print(each_item.download_file)
	print(each_item.object_versions)
	"----------------------"
import boto3
print(boto3)
import os 
from os import mkdir 
os.mkdir('Sihko')
print(os.name)
print(dir(os))
# os.remove('Josh')
os.dir_list