import boto3
from botocore.exceptions import ClientError
import json

def create_rds_db_credentials(db_name, db_username, db_password,  region="us-east-1"):
    """
    Function that takes the name, username and password of an existing RSD db hosted on AWS, and creates
    a credentials for it and store it on AWS Secret Manager.
    """
    # Create an RDS client
    rds_client = boto3.client("rds", region_name=region)

    # Fetch the Rds in a region with db_name
    try:
        print("Fetching RDS instance Information...")
        response = rds_client.describe_db_instances(DBInstanceIdentifier=db_name)
        db_instances = response.get("DBInstances", [])
    except rds_client.exceptions.DBInstanceNotFoundFault:
        # Database Not found
        print(f"No DB instance found with ID: {db_name}")
        return

    # Create AWS Secrets Manager Client
    secret_client = boto3.client("secretsmanager", region_name=region)

    # Prepare Secret Information
    secret_name = f"{db_name}-creds"
    db_instance = db_instances[0]
    secret_value = json.dumps({
        "username": db_username,
        "password": db_password,
        "engine": db_instance.get("Engine"),
        "host": db_instance.get("Endpoint", {}).get("Address"),
        "port": db_instance.get("Endpoint", {}).get("Port"),
        "dbInstanceIdentifier": db_instance.get("DBInstanceIdentifier", db_name)
    })

    # Store credentials in AWS Secrets Manager
    try:
        # Try to create the secret
        secret_client.create_secret(
            Name=secret_name,
            SecretString=secret_value,
            Description=f"Credentials for RDS database: {db_name}"
        )
        print(f"Secret {secret_name} created successfully")
    except secret_client.exceptions.ResourceExistsException:
        # If secret already exists, do nothing
        print(f"Secret {secret_name} already exists")

    except ClientError as e:
        if e.response['Error']['Code'] == 'InvalidRequestException' and \
                'scheduled for deletion' in e.response['Error']['Message']:
            print(f"Secret {secret_name} already exists and is scheduled for deletion")
        else:
            raise e


# Make Function to update RDS creds
# Make Function to delete RDS creds