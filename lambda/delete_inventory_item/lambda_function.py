import boto3
import json

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Inventory")

def lambda_handler(event, context):
    item_id = event["pathParameters"]["id"]
    location_id = int(event["queryStringParameters"]["location_id"])

    table.delete_item(
        Key={
            "item_id": item_id,
            "item_location_id": location_id
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Item deleted"})
    }
