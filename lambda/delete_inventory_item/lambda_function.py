import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def lambda_handler(event, context):
    item_id = event["queryStringParameters"]["item_id"]

    table.delete_item(Key={"item_id": item_id})

    return {
        "statusCode": 200,
        "body": "Item deleted"
    }
