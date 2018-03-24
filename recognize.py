import boto3
from boto3  import client
import pprint

bucket_name='arthur-memes'
conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3

if __name__ == "__main__":
    client=boto3.client('rekognition','us-west-2')
    photos = []

    for key in conn.list_objects(Bucket=bucket_name)['Contents']:
        key = key["Key"]
        response = client.detect_text(Image={'S3Object':{'Bucket':bucket_name,'Name':key}})
        text = []
        for txt in response["TextDetections"]:
            if "ParentId" not in txt:
               text.append(txt["DetectedText"])
        photos.append({"name": key, "text": text})
        print({"name": key, "text": text})
