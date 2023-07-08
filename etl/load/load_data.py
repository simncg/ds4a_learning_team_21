import boto3
import json 
import os
import logging


class DataLoader:
    def __init__(self) -> None:
        pass
    def create_bucket(self, bucket_name, region=None):
        try:
            if region is None:
                s3_client = boto3.client('s3', verify = False)
                s3_client.create_bucket(Bucket=bucket_name)
            else:
                s3_client = boto3.client('s3', region_name=region)
                location = {'LocationConstraint': region}
                s3_client.create_bucket(Bucket=bucket_name,
                                        CreateBucketConfiguration=location)
        except Exception as e:
            logging.error(e)
            return False
        return True
    
    def create_folder(self, bucket_name, folder_name):
        s3_client = boto3.client('s3', verify = False)
        folder_name = folder_name if folder_name.endswith('/') else folder_name + '/'
        try:
            s3_client.put_object(Bucket=bucket_name, Key=(folder_name))
        except Exception as e:
            logging.error(e)
            return False
        return True

    # Upload a file from local system.
    def upload_file(self, file_name, bucket, object_name=None):
        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = os.path.basename(file_name)

        # Upload the file
        s3_client = boto3.client('s3', verify = False)
        try:
            response = s3_client.upload_file(file_name, bucket, object_name)
        except Exception as e:
            logging.error(e)
            return False
        return True

    # Download a file from a S3 bucket.
    def download_file(self, file_name, bucket, object_name):
        s3_client = boto3.client('s3', verify = False)
        try:
            s3_client.download_file(bucket, object_name, file_name)
        except Exception as e:
            logging.error(e)
            return False
        return True

    # Delete a file from a S3 bucket.
    def delete_file(self, bucket, key_name):
        s3_client = boto3.client('s3', verify = False)
        try:
            s3_client.delete_object(Bucket=bucket, Key=key_name)
        except Exception as e:
            logging.error(e)
            return False
        return True

    # Delete bucket empty bucket
    def delete_bucket(self, bucket):
        s3_client = boto3.client('s3', verify = False)
        try:
            bucket = s3_client.delete_bucket(Bucket=bucket)
        except Exception as e:
            logging.error(e)
            return False
        return True


    