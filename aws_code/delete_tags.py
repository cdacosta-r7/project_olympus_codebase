import boto3

ec2_client = boto3.client('ec2')
response = ec2_client.describe_instances()
instances = response['Reservations']

delete_key = input('What tag do you want to delete? ')

instance_ids = []

for instance in instances:
    instance_ids.append(instance['Instances'][0]['InstanceId'])

tag_deletion = ec2_client.delete_tags(
    Resources = 
        instance_ids,
    Tags = [
        {
            'Key':delete_key
        }
    ]
)

print("Successfully Deleted Tag on Instances")