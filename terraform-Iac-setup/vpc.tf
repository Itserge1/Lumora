variable "vpc_cidr_block" {}
variable "private_subnet_cidr_blocks" {}
variable "public_subnet_cidr_blocks" {}

# Dynamically query the list of Availability zones (azs)
data "aws_availability_zones" "azs" {}

# Always get the first 3 available azs in asc order (eg: us-east-1a, us-east-1b, us-east-1c)
# for region with less than 3 az just take all
locals {
  selected_azs = slice(sort(data.aws_availability_zones.azs.names), 0, min(3, length(data.aws_availability_zones.azs.names)))
}

module "lumora-vpc" {
  source = "terraform-aws-modules/vpc/aws"
  version = "6.4.0"

  # VPC ans Subnets Information
  name            = "lumora-vpc"
  cidr            = var.vpc_cidr_block
  private_subnets = var.private_subnet_cidr_blocks
  public_subnets = var.public_subnet_cidr_blocks

  # Get a list of Availability
  azs = local.selected_azs

  # Enable NAT Gateway and DNS Hostnames
  enable_nat_gateway   = true
#   single_nat_gateway   = true # one NAT Gateway for all public subnet in every AZ in this case (3)
  single_nat_gateway = false # One NAT Gateway in each public subnet in every AZ
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Environment = "dev"
    Application = "lumora"
  }
}

