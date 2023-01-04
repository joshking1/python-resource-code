#!/usr/bin/env python3

import boto3

from boto3 import session

print(boto3)

aws_con_man = boto3.session.Session(profile_name = 'root')
aws_ec2_con = aws_con_man.client(service_name = 'ec2',region_name = 'us-east-2')

response = aws_ec2_con.create_key_pair(
    KeyName='crissy-awskeypair',
)

print(response)


