import boto3
import json
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
import requests

session = boto3.Session()
credentials = session.get_credentials()
creds = credentials.get_frozen_credentials()

region = 'eu-west-2'
service = 'es'

host = 'https://search-movies-cnl2tufhuy2b6m5ty6bisa2234.eu-west-2.es.amazonaws.com'
index = 'movies'
url = host + '/' + index + '/_search'

def signed_request(method, url, data=None, params=None, headers=None):
    request = AWSRequest(method=method, url=url, data=data, params=params, headers=headers)
    SigV4Auth(creds, service, region).add_auth(request)
    return requests.request(method=method, url=url, headers=dict(request.headers), data=data)
    
def lambda_handler(event, context):
    query = {
        "size": 25,
        "query": {
            "multi_match": {
                "query": event['queryStringParameters']['q'],
                "fields": ["title^4"]
            }
        }
    }

    headers = { "Content-Type": "application/json" }

    r = signed_request(method='GET', url=url, data=json.dumps(query), headers=headers)

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": '*'
        },
        "isBase64Encoded": False
    }

    response['body'] = r.text
    return response