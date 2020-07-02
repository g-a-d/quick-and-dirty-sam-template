import json
import boto3
import urllib

def lambda_handler(event, context):
    record = event['Records'][0]
    try:
        if 'aws:sns' == record['EventSource'] and record['Sns']['Message']:
            record = json.loads(record['Sns']['Message'])['Records'][0]
    except KeyError:
        pass

    bucket = record['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(record['s3']['object']['key'], encoding='utf-8')
    print("got event for {}/{}".format(bucket,key))
    
