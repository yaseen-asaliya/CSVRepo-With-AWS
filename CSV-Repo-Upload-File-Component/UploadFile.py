import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    body = event['body']
    filename = event['queryStringParameters']['filename']
    
    if not filename.endswith('.csv'):
        return {
            'statusCode': 400,
            'body': 'File must be a CSV'
        }
    
    s3.put_object(Bucket='csvrepo-s3-yaseen', Key=filename, Body=body)

    return {
        'statusCode': 200,
        'body': 'File uploaded successfully'
    }
