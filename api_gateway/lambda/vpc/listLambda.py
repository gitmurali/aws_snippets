import json
import boto3

client = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table_name = "userdbtable"
    table = client.Table(table_name)
    response = table.scan()
    return response['Items']