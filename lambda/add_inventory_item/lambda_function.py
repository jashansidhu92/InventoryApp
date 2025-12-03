import boto3
import json
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def lambda_handler(event, context):
    body = json.loads(event["body"])

    table.put_item(Item=body)

    return {
        "statusCode": 200,
        "body": "Item added successfully"
    }
