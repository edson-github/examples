import json
import datetime


def endpoint(event, context):
    current_time = datetime.datetime.now().time()
    body = {"message": f"Hello, the current time is {str(current_time)}"}

    return {"statusCode": 200, "body": json.dumps(body)}
