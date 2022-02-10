import boto3


def get_resource():
    return boto3.resource('dynamodb',
                          aws_access_key_id='ACCESS KEY',
                          aws_secret_access_key='SECRET ACCESS KEY',
                          region_name='eu-north-1')


def get_all_readings():
    client = get_resource()
    table = client.Table('temp_readings')
    response = table.scan()
    return response['Items']