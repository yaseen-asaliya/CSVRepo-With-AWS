import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')

def lambda_handler(event, context):
    try:
        table_name = event['table_name']
    except Exception as e:
        return {
            'statusCode': 400,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': 'Invalid request body'})
        }
    
    table = dynamodb.Table(table_name)
    response = table.scan()
    items = response['Items']
    
    for item in items:
        for key in item:
            if isinstance(item[key], set):
                item[key] = list(item[key])
    
    json_data = json.dumps(items)
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json_data
    }
