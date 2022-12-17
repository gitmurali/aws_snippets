import json
import boto3
import json

client = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table_name = "userdbtable"
    table = client.Table(table_name)
    try:
        student_id = event['student_id']
        response = table.delete_item(
            Key={
                "id": student_id
            })
        return {
            "status": "200 - Success"
        }
    except Exception as e:
        return {
            "status": "400 - failed to delete item"
        }