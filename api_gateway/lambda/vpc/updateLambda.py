import json
import boto3

client = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table_name = "userdbtable"
    table = client.Table(table_name)
    
    try:
        student_id = event['student_id']
        column_name = event['table_clmn_name']
        column_value = event['table_clmn_value']
        response = table.update_item(
            Key={'id': student_id},
            UpdateExpression="SET {} = :l".format(column_name),
            ConditionExpression="attribute_exists(id)",
            ExpressionAttributeValues={':l': column_value},
            ReturnValues="ALL_NEW"
        )
        return (response['Attributes'])
    except Exception as e:
        return {
            "status": "400 - failed to update item."
        }
