import boto3

ec2_client = boto3.client('ec2')
response = ec2_client.describe_instances()
instances = response['Reservations']

instance_ids = []

""" for instance in instances:
        print(instance['Instances'][0]['InstanceId']) """

for instance in instances:
    instance_ids.append(instance['Instances'][0]['InstanceId'])


tag_creation = ec2_client.create_tags(
    Resources = 
        instance_ids,
    Tags = [
        {
            'Key':'CUSTOM_TAG',
            'Value':'Adding from Script'
        }
    ]
)

print("Successfully added Tags on Instances")

