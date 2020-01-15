import boto3
from mypy_boto3 import s3

try:
    session = boto3.session.Session()

    s3_client: s3.S3Client = session.client(
        service_name="s3",
        aws_access_key_id="123",
        aws_secret_access_key="123",
        endpoint_url="http://localstack:4572",
    )

    bucket_test1 = s3_client.create_bucket(Bucket="test1")
    bucket_test2 = s3_client.create_bucket(Bucket="test2")

    response = s3_client.list_buckets()
    buckets = [bucket["Name"] for bucket in response["Buckets"]]
    print(f"list buckets created: {buckets}")
    if ["test1", "test2"] in buckets:
        raise Exception("Test bucket not created")

    s3_client.delete_bucket(Bucket="test1")
    s3_client.delete_bucket(Bucket="test2")

    response = s3_client.list_buckets()
    buckets = [bucket["Name"] for bucket in response["Buckets"]]
    print(f"list buckets after delete: {buckets}")

except Exception as e:
    print(f"Error: {e}")
