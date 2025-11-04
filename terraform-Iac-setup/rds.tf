
variable "db_name" {}
variable "db_username" {}
variable "db_password" {}
variable "my_ip" {}
variable "snapshot_identifier" {
  description = "RDS snapshot name to restore from (optional)"
  type        = string
  default     = ""
}

resource "aws_db_subnet_group" "rds_subnet_group" {
  name       = "rds-subnet-group"
  subnet_ids = module.lumora-vpc.private_subnets

  tags = {
    Name = "rds-subnet-group"
  }
}

resource "aws_security_group" "rds_sg" {
  name        = "rds-sg"
  description = "Allow SQL traffic from My Ip and VPN clients"
  vpc_id      = module.lumora-vpc.vpc_id

    # From VPN clients
    ingress {
      from_port                = 1433
      to_port                  = 1433
      protocol                 = "tcp"
      description              = "Allow MSSQL from VPN clients"
      security_groups          = [aws_security_group.client_vpn_sg.id]
    }

  # From your own IP (local dev)
  ingress {
    from_port   = 1433
    to_port     = 1433
    protocol    = "tcp"
    cidr_blocks = ["${var.my_ip}/32"]
    description = "Allow MSSQL from my IP"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "rds-sg"
  }
}

resource "aws_db_instance" "sql_server" {
  identifier              = var.db_name
  instance_class          = "db.t3.micro"
  storage_type            = "gp2"

  # Conditionally use snapshot if provided
  snapshot_identifier     = var.snapshot_identifier != "" ? var.snapshot_identifier : null

  # Only set these if no snapshot provided
  engine                  = var.snapshot_identifier == "" ? "sqlserver-ex" : null
  engine_version          = var.snapshot_identifier == "" ? "15.00.4073.23.v1" : null
  allocated_storage       = var.snapshot_identifier == "" ? 20 : null
  username                = var.snapshot_identifier == "" ? var.db_username : null
  password                = var.snapshot_identifier == "" ? var.db_password : null

  db_subnet_group_name    = aws_db_subnet_group.rds_subnet_group.name
  vpc_security_group_ids  = [aws_security_group.rds_sg.id]

  multi_az                = false
  publicly_accessible     = false
  skip_final_snapshot     = true
  deletion_protection     = false

  tags = {
    Name        = var.db_name
    Environment = "dev"
  }
}


# Create a python cli tool that check if the name of the snapshot mane you pass actually exist on aws if not the it will
# update the variable snapshot_identifier to ""