import boto3
import time

ec2_client = boto3.client('ec2')
instances = [i for i in boto3.resource('ec2', region_name='us-west-1').instances.all()]

# What tag do we want to check against
check_tag = input('What tag do you want to validate? ')
set_value = input('Enter a value for the above key: ')

untagged_instances = []

# This will check if instances in a region have a certain tag FAKE
for i in instances:
  if i.tags is not None and check_tag not in [t['Key'] for t in i.tags]:
   # print(i.instance_id, 'does not have the', check_tag, 'tag') 
    untagged_instances.append(i.instance_id)

print('Untagged Instances:')
print(' ',untagged_instances)

# Add a tag to the instances 

ec2_client = boto3.client('ec2')

tag_creation = ec2_client.create_tags(
    Resources = 
        untagged_instances,
    Tags = [
        {
            'Key': check_tag,
            'Value': set_value
        }
    ]
)

# Let the user know something is happening
print('Adding the', check_tag, 'tag...')
time.sleep(1)

# Let the user know that the tag has been added
print("Successfully added Tags on Instances:")
print(untagged_instances)
