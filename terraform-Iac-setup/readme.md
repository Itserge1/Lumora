# Terraform AWS Infrastructure Project

This Terraform project automates the creation of AWS infrastructure. It provisions a **VPC**, along with **three public
** and **three private subnets** across **three Availability Zones (AZs)**. Additionally, it sets up an **RDS instance**
in a private subnet and configures a **Client VPN** to securely access and protect all resources within the VPC.

## A - 🧩 Prerequisites

Before running this Terraform project, you must set up your AWS credentials using **AWS Identity Center (SSO)**.

--- 

## Set Up AWS Identity User

Contact your AWS administrator to request an **AWS Identity Center (SSO)** user account. They will provide your
credentials and access details.

### Step 1️⃣ Verify AWS CLI Installation

Ensure that **AWS CLI version 2** is installed on your system:

```bash
aws --version
```

You should see output similar to:

```
aws-cli/2.17.0 ...
```

If not, download and install AWS CLI v2
from [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

### Step 2️⃣ Gather Your AWS SSO Details

You’ll need the following information from your AWS administrator or AWS console:

| Detail             | Example                                   |
|:-------------------|:------------------------------------------|
| **SSO Start URL**  | `https://my-sso-portal.awsapps.com/start` |
| **SSO Region**     | `us-east-1`                               |
| **AWS Account ID** | `999999999999`                            |
| **Role Name**      | `AdministratorAccess`                     |

### Step 3️⃣ Configure AWS CLI for SSO

Run the following command to set up your local AWS CLI profile:

```bash
aws configure sso
```

When prompted, provide the following details:

```
SSO session name (Recommended): my-sso-session
SSO start URL [None]: https://my-sso-portal.awsapps.com/start
SSO region [None]: us-east-1   # (Use the same region as your Terraform project)
SSO registration scopes [None]: sso:account:access
```

You’ll then be prompted to choose your AWS account and role.
Select your assigned AWS account (press Enter if it auto-selects) and choose your **AdministratorAccess** role.

Once configured, you can verify your settings by running:

```bash
cat ~/.aws/config
```

### Step 4️⃣ Log In to AWS SSO

Use your SSO profile to authenticate:

```bash
aws sso login --profile AdministratorAccess-999999999999
```

### Step 5️⃣ Test Your AWS Profile

To confirm everything is working, try listing your S3 buckets:

```bash
aws s3 ls --profile AdministratorAccess-999999999999
```

If this command lists your S3 buckets (or no buckets but no error), your AWS credentials are correctly configured 🎉

Your machine can now securely access AWS using AWS Identity Center credentials.

## B - 🚀 Run the Terraform Project

1. Open the `main.tf` file.
2. Update the provider block with your profile and region:

    ```hcl
    provider "aws" {
      region  = "us-east-1"
      profile = "AdministratorAccess-999999999999"
    }
    ```

3. **Initialize and plan the Terraform configuration:**

   ```bash
   terraform init --upgrade
   ```

4. **Update or create your `terraform-Iac-setup/terraform.tfvars` file** with the following values:

   ```hcl
   vpc_cidr_block="10.0.0.0/16"
   private_subnet_cidr_blocks=["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
   public_subnet_cidr_blocks=["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]
   snapshot_identifier = "database-test-1-2025-10-04"
   vpn_client_cidr    = "172.16.0.0/19"
   
   db_username = ""   # Get from your Admin
   db_password = ""   # Get from your Admin
   my_ip       = ""   # Your current public IP
   ```

   > 💡 **Tip:**
   >
   > * You can find your current IP by visiting [https://whatismyipaddress.com/](https://whatismyipaddress.com/).
   > * Ask your Admin for the **database username** and **password**.

5. **Plan the Terraform configuration** after updating `terraform.tfvars`:

   ```bash
   terraform plan
   ```
   
   This will show you a preview of the infrastructure Terraform will create or modify based on your configuration.

6. **Apply** the Terraform configuration to deploy your infrastructure:

   ```bash
   terraform apply --auto-approve
   ```

   This will provision your **VPC**, **subnets**, **RDS instance**, and **Client VPN**.

   ✅ **You’re all set!**
   Your AWS infrastructure is now created automatically through Terraform using secure SSO authentication.

7. **When you’re done**, make sure to **⚠️ DESTROY** the infrastructure, I don’t have money for surprise AWS bills 😅

   ```bash
   terraform destroy --auto-approve
   ```

   This command will clean up all the resources created by Terraform.

**FYI:** If `terraform apply` or `terraform destroy` fails due to a timeout, make sure you are **NOT connected to the VPN**
and try running the command again.

⚠️ The process can be a bit flaky at times. The DevOps team (aka MOI) is currently working on improving reliability.

---

## C - 🚀 Access Resources

In this section, we’ll explain how to access resources created by this Terraform project.

### 🔑 Connect to the RDS

To connect to the RDS instance, you must first connect to the **VPN**:

1. **Request VPN access:**
   Contact your AWS administrator to provide a **Client VPN configuration** and create a **Client VPN user** for you.

2. **Install the VPN client:**
   Download and install the **AWS VPN Client** app. This will allow you to securely connect to the VPC.

3. **Connect to the VPN:**
   Use the credentials and configuration provided by your admin to establish a VPN connection.

4. **Connect to RDS using your database client:**
   Once connected to the VPN, you can access the RDS instance using your preferred database management tool, such as *
   *MS SQL Server Management Studio**, **DataGrip**, or any other client.

✅ **Tip:** Always make sure the VPN connection is active before attempting to access the RDS instance.

