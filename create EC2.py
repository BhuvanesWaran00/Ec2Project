import boto3

def create_ec2_instance():
    try:
        # Replace 'us-east-1' with the AWS region you want to create the EC2 instance in (e.g., 'us-east-1', 'eu-west-1', etc.)
        region_name = 'us-east-1'

        # Create a Boto3 EC2 client using the session
        ec2_client = boto3.client('ec2', region_name=region_name)

        # Specify the parameters for the EC2 instance
        instance_params = {
            'ImageId': 'ami-05548f9cecf47b442',    # Replace 'ami-05548f9cecf47b442 ' with the AMI ID you want to use (e.g., 'ami-xxxxxxxxxxxxxxxxx')
            'InstanceType': 't2.micro',  # Replace 't2.micro' with the instance type you want to use (e.g., 't2.micro', 't2.small', etc.)
            'KeyName': '123',  # Replace 'your_key_pair_name' with the name of the key pair you want to use
            'MinCount': 1,
            'MaxCount': 1,
        }

        # Create the EC2 instance
        response = ec2_client.run_instances(**instance_params)

        # Extract the instance ID from the response
        instance_id = response['Instances'][0]['InstanceId']

        print(f"EC2 instance with ID {instance_id} is being created.")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    create_ec2_instance()
