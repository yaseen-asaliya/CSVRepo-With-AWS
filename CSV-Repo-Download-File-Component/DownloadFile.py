import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = 'csvrepo-s3'
    file_name = event['queryStringParameters']['KeyName']
    expiration_seconds = 3600

    try:
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket_name,
                'Key': file_name
            },
            ExpiresIn=expiration_seconds
        )
        print(f'File downloaded successfully: {file_name}')
        return {
            'link': url
        }
    except Exception as e:
        print(f'Error downloading file: {e}')
        raise e
