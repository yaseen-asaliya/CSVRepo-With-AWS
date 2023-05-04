import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        bucket_name = 'csv-repo-s3-yaseen'
        
        response = s3.list_objects(Bucket=bucket_name)
        files = [{'file': obj['Key']} for obj in response['Contents']]
        
        return {
            'statusCode': 200,
            'body': json.dumps(files)
        }
        
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error retrieving files from S3'})
        }