import boto3


def list_files(bucket_name: str):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    for file in bucket.objects.all():
        print(f'File: {file.key}')