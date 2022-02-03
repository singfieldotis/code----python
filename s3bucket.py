import sys

import boto3

try:
    def main():
        create_s3bucket(bucket_name)

except Exception as e:
    print(e)


def create_s3bucket(bucket_name):
    s3bucket = boto3.client(
        's3',
    )

    bucket = s3bucket.create_bucket(
        Bucket=bucket_name,
        ACL='private',
    )

    print(bucket)


bucket_name = sys.argv[1]

if __name__ == '__main__':
    main()
