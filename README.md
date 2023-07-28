## Integrating Python with AWS EC2
### Table of Contents
+ Prerequisites
+ AWS Toolkit for Visual Studio Code
+ Checking AWS Connection with Python
+ Creating EC2 Instances using Python

### Prerequisites
Before proceeding, make sure you have the following installed and configured:
+ Visual Studio Code: You can download it from the official website: Visual Studio Code (If you want You can use any Text Editor)
+ Python: Ensure Python is installed on your system.
+ AWS CLI and Credentials: Set up the AWS CLI on your machine and configure your AWS credentials. You can do this by running aws configure in your terminal and providing your AWS Access Key ID, AWS Secret Access Key, default region, and default output format.
### AWS Toolkit for Visual Studio Code
+ Ensure your AWS credentials are properly configured in your environment using the AWS CLI or environment variables.
+ Add AWS Toolkit using this link:
  
  [https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.AWSToolkitforVisualStudio2022]
+ Click on the AWS icon in the VS Code Activity Bar to access the AWS Explorer panel. Here, you can set AWS Toolkit preferences and manage AWS services.
### Checking AWS Connection with Python
The next step is to verify the connection between AWS and Python using the boto3 library.
1. Ensure you have boto3 installed. You can install it using the following command: **pip install boto3**
2. Use the boto3 library to check your AWS connection by running the provided Python script: **check_con.py**
### Creating EC2 Instances using Python
+ Run the provided Python script:**create EC2.py** to create an EC2 instance with your desired parameters.
+ Customize the script to include the AMI ID, instance type, and key pair name.
