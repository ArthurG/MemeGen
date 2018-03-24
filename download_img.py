import pandas as pd
import time
import requests

import boto3

s3 = boto3.resource('s3')

def download(image_url, title):
    img_data = requests.get(image_url).content
    with open("photos/"+title, 'wb') as handler:
        handler.write(img_data)

df = pd.read_csv("dec17scrape.csv")
imgs = []
for url, score in zip(df["url"], df["score"]):
    t = time.time()
    if url.endswith(".jpg"):
        img = "{}_{}.jpg".format(t, score)
    elif url.endswith(".png"):
        img = "{}_{}.jpg".format(t, score)
    try:
        download(url, img)
        data = open('photos/' + img, 'rb')
        s3.Bucket("arthur-memes").put_object(Key=img, Body=data)
    except:
        print('An error occurred.')

