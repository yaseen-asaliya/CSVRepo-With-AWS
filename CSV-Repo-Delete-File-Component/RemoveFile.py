import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    file_name =  event['file_name']
    
    bucket_name = 'csvrepo-s3-yaseen'
    
    s3.delete_object(Bucket=bucket_name, Key=file_name)
    
    return {
        'statusCode': 200,
        'file_name': file_name,
        'body': f'File {file_name} removed successfully from S3 bucket!'
    }
