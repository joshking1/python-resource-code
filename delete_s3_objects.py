#!/usr/bin/env python3

import boto3

from boto3 import session

print(boto3)

aws_con_man = boto3.session.Session(profile_name = 'root')
aws_S3_con = aws_con_man.client(service_name = 's3',region_name = 'us-east-2')

response = aws_S3_con.delete_object(
    Bucket='caleb-s3-bucket',
    Key='Centos.ova',
)

print(response)