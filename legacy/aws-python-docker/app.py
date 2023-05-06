import json


def handler(event, context):
    body = {
        "message": "Hello, world! Your function executed successfully!",
    }

    return {"statusCode": 200, "body": json.dumps(body)}
