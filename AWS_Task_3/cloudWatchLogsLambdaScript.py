#Lambda Script to View S3 Logs in CloudWatch:

import json
import boto3
import logging
import os

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Received event: %s", json.dumps(event))

    # Parse event from S3
    for record in event.get("Records", []):
        if record.get("eventSource") == "aws:s3":
            bucket_name = record["s3"]["bucket"]["name"]
            object_key = record["s3"]["object"]["key"]
            event_name = record["eventName"]
            event_time = record["eventTime"]
            log_entry = {
                "event": event_name,
                "bucket": bucket_name,
                "object": object_key,
                "timestamp": event_time
            }
            logger.info("S3 Change Detected: %s", json.dumps(log_entry))

    return {
        "statusCode": 200,
        "body": json.dumps("S3 Event Processed Successfully")
    }
