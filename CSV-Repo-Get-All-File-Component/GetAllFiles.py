import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        bucket_name = 'csvrepo-s3-yaseen'  
        response = s3.list_objects(Bucket=bucket_name)   
        
        if len(response.get('Contents', [])) == 0:
            return {
                'statusCode': 200,
                'body': 'Database is empty'
            }
        else:
            files = [{'file': obj['Key']} for obj in response['Contents']]
            return {
                'statusCode': 200,
                'body': json.dumps(files)
            }
     
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'error': f"{e}",
            'body': json.dumps({'message': 'Error retrieving files from S3'})
        }
