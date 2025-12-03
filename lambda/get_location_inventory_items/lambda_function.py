import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def lambda_handler(event, context):
    location_id = event["queryStringParameters"]["location_id"]

    response = table.query(
        IndexName="location_id-index",
        KeyConditionExpression=boto3.dynamodb.conditions.Key("location_id").eq(location_id)
    )

    return {
        "statusCode": 200,
        "body": response.get("Items", [])
    }
