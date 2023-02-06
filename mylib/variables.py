import os

# Environment variables
ACCESS_KEY_SQS = os.getenv("ak_sqs")
SECRET_KEY_SQS = os.environ.get("sk_sqs")
ACCESS_KEY_S3 = os.getenv("ak_s3")
SECRET_KEY_S3 = os.environ.get("sk_s3")


#SQS variables
sqs_link = "https://sqs.us-east-1.amazonaws.com/492094906798/"

# Variables
LinksCount = 0
count = 0
SearchingFor = []
LinksSearched = []
l = set()
NotFoundLink = set()
links = set()
Nooflinkssearched = []
