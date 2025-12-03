import boto3
import json
import ulid

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Inventory")

def lambda_handler(event, context):
    body = json.loads(event["body"])

    new_item = {
        "item_id": str(ulid.ULID()),  # generate unique ID
        "item_location_id": int(body["item_location_id"]),
        "item_name": body["item_name"],
        "item_description": body["item_description"],
        "qty_on_hand": int(body["qty_on_hand"]),
        "item_price": float(body["item_price"])
    }

    table.put_item(Item=new_item)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Item added", "item": new_item})
    }
