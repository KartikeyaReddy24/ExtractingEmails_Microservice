# SQS CODE HERE
# CONNECTION TO AWS VIA BOTO3 'CLIENT'
import boto3
import time
import requests
from mylib.variables import *

start_time = time.time()

def sqs_queue():

    client = boto3.resource(
        "sqs",
        aws_access_key_id=ACCESS_KEY_SQS,
        aws_secret_access_key=SECRET_KEY_SQS,
        region_name="us-east-1",
    )

    print("##########################################")
    print("AVAILABLE QUEUES : URLS")
    queues=[]
    for queue in client.queues.all():
        print(queue.url)
        queues.append(queue.url)
    print("##########################################")

    # SQS SEND OR RECEIVE

    url = sqs_link + str("CollegePrductionService")
    # return url
    receipt = sqs_queue.client.Queue(url=url).receive_messages(
    MaxNumberOfMessages=2
    )
    req_session = requests.session()
    return receipt
