import boto3

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb')
    
    table_name = event['Records'][0]['s3']['object']['key']
    table_name = table_name[:-4]
    
    try:
        response = dynamodb.delete_table(TableName=table_name)
        return {
            'statusCode': 200,
            'body': f'Table {table_name} deleted successfully'
        }
    except dynamodb.exceptions.ResourceNotFoundException:
        return {
            'statusCode': 404,
            'body': f'Table {table_name} not found'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
