import boto3
import uuid
from botocore.exceptions import NoCredentialsError
from mylib.variables import *


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client(
        "s3", aws_access_key_id=ACCESS_KEY_S3, aws_secret_access_key=SECRET_KEY_S3
    )

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("\t\tUpload Successful")
        return True
    except FileNotFoundError:
        print("\t\tThe file was not found")
        return False
    except NoCredentialsError:
        print("\t\tCredentials not available")
        return False


file_name = str(uuid.uuid4().hex)
print("\n\t\tThe File name alloted: ", file_name)

for file in os.listdir():
    if file.endswith(str(file_name) + ".xlsx"):
        print("\n\tThis is the file:::::::::::::::", file)
        print("\n\n\t\t", os.path.dirname(os.path.realpath(__file__)))
        uploaded = upload_to_aws(
            os.path.dirname(os.path.realpath(__file__)) + "/" + file,
            "extract.emails.storage",
            "College_ProductionService/" + file,
        )
