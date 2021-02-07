import json
from Books import get


def lambda_handler(event, context):
    # TODO implement
    r = get()
    print(r)
    return {
        'statusCode': 200,
        'body': r
    }
