import boto3
s3 = boto3.client('s3')
s3.create_bucket(Bucket='pearl1234567',
    CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
