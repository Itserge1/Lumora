import boto3
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
    secret_name = f"{db_name}-credentials"
    db_instance = db_instances[0]
    secret_value = json.dumps({
        "username": db_username,
        "password": db_password,
        "host": db_instance.get("Endpoint", {}).get("Address"),
        "port": db_instance.get("Endpoint", {}).get("Port"),
        "db_name": db_instance.get("DBName")
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


# Make Function to update RDS creds
# Make Function to delete RDS creds