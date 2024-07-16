# Date:   03/08/2015
# Author: Long Chen
# Description: A class to establish connections to aws services

import boto3

class awsConnection:
    _aws_connection = None

    def __init__(self):
        _aws_connection = None

    # CloudWatch connection
    def cloudwatchConnect(self, region, access_key, secret_key):
        session = boto3.session.Session(aws_access_key_id = access_key, aws_secret_acces_key = secret_key, region_name = region)
        self._aws_connection = session.client('cloudwatch')

    # ELB connection
    def elbConnect(self, region, access_key, secret_key):
        session = boto3.session.Session(aws_access_key_id = access_key, aws_secret_acces_key = secret_key, region_name = region)
        self._aws_connection = session.client('elb')

    # SQS connection
    def sqsConnect(self, region, access_key, secret_key):
        session = boto3.session.Session(aws_access_key_id = access_key, aws_secret_acces_key = secret_key, region_name = region)
        self._aws_connection = session.client('sqs')

    # RDS connection
    def rdsConnect(self, region, access_key, secret_key):
        session = boto3.session.Session(aws_access_key_id = access_key, aws_secret_acces_key = secret_key, region_name = region)
        self._aws_connection = session.client('rds')

    # DynamoDB connection
    def dynamodbConnect(self, region, access_key, secret_key):
        session = boto3.session.Session(aws_access_key_id = access_key, aws_secret_acces_key = secret_key, region_name = region)
        self._aws_connection = session.client('dynamodb')

    # Redshift connection
    def redshiftConnect(self, region, access_key, secret_key):
        session = boto3.session.Session(aws_access_key_id = access_key, aws_secret_acces_key = secret_key, region_name = region)
        self._aws_connection = session.client('redshift')

    # SNS connection
    def snsConnect(self, region, access_key, secret_key):
        session = boto3.session.Session(aws_access_key_id = access_key, aws_secret_acces_key = secret_key, region_name = region)
        self._aws_connection = session.client('sns')

    # Route53 connection
    def route53Connect(self, region, access_key, secret_key):
        session = boto3.session.Session(aws_access_key_id = access_key, aws_secret_acces_key = secret_key, region_name = region)
        self._aws_connection = session.client('route53')

    # EMR connection
    def emrConnect(self, region, access_key, secret_key):
        session = boto3.session.Session(aws_access_key_id = access_key, aws_secret_acces_key = secret_key, region_name = region)
        self._aws_connection = session.client('emr')
