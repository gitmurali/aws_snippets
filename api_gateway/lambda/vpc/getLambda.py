import os
import json
import boto3

client = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table_name = "userdbtable"
    table = client.Table(table_name)
    try:
        student_id = event['student_id']
        response = table.get_item(Key={
            "id": student_id
        })
        return (response['Item'])
    except Exception as e:
        return {
            "status": "400 - failed to retrieve item by id"
        }