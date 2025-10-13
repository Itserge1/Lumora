variable "vpn_client_cidr" {}

locals {
  # find first private subnet with a NAT route
  private_subnet_with_nat = module.lumora-vpc.private_subnets[0] # this subnet must have NAT
  # If using multiple NATs (single_nat_gateway=false), you could map AZs dynamically
}


resource "aws_security_group" "client_vpn_sg" {
  name        = "client-vpn-sg"
  description = "Allow VPN client traffic"
  vpc_id      = module.lumora-vpc.vpc_id

  ingress {
    from_port   = 1433
    to_port     = 1433
    protocol    = "tcp"
    cidr_blocks = [var.vpn_client_cidr]
    description = "Allow VPN clients to access Microsoft SQL Server"
  }

  egress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "client-vpn-sg"
  }
}

resource "aws_ec2_client_vpn_endpoint" "vpn" {
  description = "Client VPN for accessing RDS"
  # Server Cert uploaded on aws ACM
  server_certificate_arn = "arn:aws:acm:us-east-1:318526443004:certificate/bbeccc21-0f62-4807-9129-80c3cc6b6b4d"
  client_cidr_block      = var.vpn_client_cidr
  authentication_options {
    type = "certificate-authentication"
    # Client Cert uploaded on aws ACM
    root_certificate_chain_arn = "arn:aws:acm:us-east-1:318526443004:certificate/728e93b3-3134-4810-a54f-12ee2d99d8b3"
  }

  # AWS’s internal DNS (10.0.0.2) to resolve private hostnames like the RDS endpoint IMPORTANT
  dns_servers = ["10.0.0.2"]

  connection_log_options {
    enabled = false
  }

  split_tunnel = true
  vpc_id       = module.lumora-vpc.vpc_id
  security_group_ids = [aws_security_group.client_vpn_sg.id]
  tags = {
    Name = "client-vpn-endpoint"
  }
}

# Associate VPN with private subnets
# Associate a Target Network (The VPC in witch the RDS Database reside)
resource "aws_ec2_client_vpn_network_association" "vpn_assoc" {
  client_vpn_endpoint_id = aws_ec2_client_vpn_endpoint.vpn.id
  count = length(module.lumora-vpc.private_subnets)
  subnet_id              = module.lumora-vpc.private_subnets[count.index]
}

# Authorization for VPC access
# Add Authorization rule for a specify the destination network (your VPC cidr)
# What this part is saying is: Resources a that destination network should be allowed to a user group we will specify,
# In this case we are allowing access to all user, because we are using certification base auth here. So every user that
# have the right certificate can access the Target Destination network (our VPC)
resource "aws_ec2_client_vpn_authorization_rule" "vpn_auth" {
  client_vpn_endpoint_id = aws_ec2_client_vpn_endpoint.vpn.id
  target_network_cidr    = var.vpc_cidr_block
  authorize_all_groups   = true
}

resource "null_resource" "vpn_delay" {
  # Use a local-exec to sleep for N seconds
  provisioner "local-exec" {
    command = "sleep 240" # wait 4 minutes
  }
}

# VPN route to Internet (must use private subnet with NAT Gateway)
resource "aws_ec2_client_vpn_route" "internet_access" {
  client_vpn_endpoint_id = aws_ec2_client_vpn_endpoint.vpn.id
  destination_cidr_block = "0.0.0.0/0"
  target_vpc_subnet_id   = local.private_subnet_with_nat
  depends_on = [null_resource.vpn_delay]
}

resource "aws_ec2_client_vpn_authorization_rule" "internet_access" {
  client_vpn_endpoint_id = aws_ec2_client_vpn_endpoint.vpn.id
  target_network_cidr    = "0.0.0.0/0"
  authorize_all_groups   = true
  description            = "Allow internet access"
}




