import boto3
import csv

s3_client = boto3.client('s3')
dynamo_db = boto3.resource('dynamodb', region_name='eu-west-2')
lambda_client = boto3.client('lambda')

def lambda_handler(event, context):
    try:
        table_name = event['Records'][0]['s3']['object']['key']
        bucket_name = event['Records'][0]['s3']['bucket']['name']

        response = s3_client.get_object(Bucket=bucket_name, Key=table_name)
        lines = response['Body'].read().decode('utf-8').splitlines()

        table_name = table_name[:-4]
        headers = lines[0].split(',')
        
        existing_tables = dynamo_db.meta.client.list_tables()['TableNames']
        if table_name not in existing_tables:
            key_schema = [
                {
                    'AttributeName': headers[0],
                    'KeyType': 'HASH'
                }
            ]
            attribute_definitions = [
                {
                    'AttributeName': headers[0],
                    'AttributeType': 'S'
                }
            ]
            table = dynamo_db.create_table(
                TableName=table_name,
                KeySchema=key_schema,
                AttributeDefinitions=attribute_definitions,
                BillingMode='PAY_PER_REQUEST'
            )
            table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
        
        table = dynamo_db.Table(table_name)
        with table.batch_writer() as batch:
            for row in csv.DictReader(lines[1:], fieldnames=headers):
                batch.put_item(Item=row)
                
        return {
            'statusCode': 200,
            'body': 'CSV data stored in DynamoDB'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
