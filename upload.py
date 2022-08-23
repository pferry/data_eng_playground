import boto3

def upload_file(bucket,file,data):
    client = boto3.client('s3')
    
    response = client.put_object(
    Body=data,
    Bucket=bucket,
    Key=file
    )
    return response