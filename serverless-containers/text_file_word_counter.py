import boto3
import os
import urllib.parse

s3 = boto3.client("s3")
sns = boto3.client("sns")

SNS_TOPIC_ARN = os.environ["topicARN"]

def lambda_handler(event, context):
    for record in event["Records"]:
        bucket_name = record["s3"]["bucket"]["name"]
        object_key = urllib.parse.unquote_plus(
            record["s3"]["object"]["key"]
        )

        response = s3.get_object(
            Bucket=bucket_name,
            Key=object_key
        )

        text = response["Body"].read().decode("utf-8")
        word_count = len(text.split())

        message = (
            f"The word count in the {object_key} file is "
            f"{word_count}."
        )

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="Word Count Result",
            Message=message
        )

        print(message)

    return {
        "statusCode": 200,
        "body": "Word count completed successfully."
    }