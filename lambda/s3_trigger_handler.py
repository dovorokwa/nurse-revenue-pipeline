# s3_trigger_handler.py
# AWS Lambda function triggered by new S3 objects

import json

def lambda_handler(event, context):
    print("New file uploaded to S3. Event data:")
    print(json.dumps(event))
    # Add logic to trigger AWS Glue Job or Step Function
