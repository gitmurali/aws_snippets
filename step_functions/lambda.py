import json

def lambda_handler(event, context):

    return {
        'statusCode': 200,
        'body': json.dumps("You have invoked lambda function from Step Function successfully")
    }