import json
import boto3

region = 'eu-west-2'

ec2 = boto3.client('ec2', region_name=region)

def get_instance_ids(instance_names):

    all_instances = ec2.describe_instances()
    instance_ids = []
    
    for instance_name in instance_names:
        for reservation in all_instances['Reservations']:
            for instance in reservation['Instances']:
                if 'Tags' in instance:
                    for tag in instance['Tags']:
                        if tag['Key'] == 'Name' \
                            and tag['Value'] == instance_name:
                            instance_ids.append(instance['InstanceId'])
                            
    return instance_ids

def lambda_handler(event, context):
    instance_names = event["Instances"].split(',')
    action = event["action"]
    
    instance_ids = get_instance_ids(instance_names)
    
    response = ''
    if action == 'Start':
        print("STARTing your instances: " + str(instance_ids))
        ec2.start_instances(InstanceIds=instance_ids)
        response = "Successfully started instances: " + str(instance_ids)
    elif action == 'Stop':
        print("STOPping your instances: " + str(instance_ids))
        ec2.stop_instances(InstanceIds=instance_ids)
        response = "Successfully stopped instances: " + str(instance_ids)
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }