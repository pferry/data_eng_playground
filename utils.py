from datetime import datetime, timedelta
import os
import boto3,botocore

EXTENSION='.json.gz'


def get_next_file(filename):
    date_part = filename.split('.')[0]
    date = datetime.strptime(date_part,"%Y-%m-%d-%H") + timedelta(hours=1)
    return f'{datetime.strftime(date,"%Y-%m-%d-%-H")}{EXTENSION}'

def get_bookmark(bucket,bookmark,file_prefix,baseline_file):
    client = boto3.client("s3")
    try:
        response = client.get_object(
            Bucket=bucket,
            Key=f'{file_prefix}/{bookmark}',
        )
    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'NoSuchKey':
            return baseline_file
        else:
            raise error
    return response['Body'].read().decode('utf-8')