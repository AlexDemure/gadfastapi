from gads3 import S3
from src.framework import settings

s3 = S3(
    bucket=settings.S3_BUCKET,
    endpoint_url=settings.S3_HOST,
    aws_access_key_id=settings.S3_ACCESS_KEY,
    aws_secret_access_key=settings.S3_SECRET_KEY,
)
