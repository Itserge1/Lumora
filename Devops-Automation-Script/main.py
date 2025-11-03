#!/usr/bin/env python3

import click
from cli.create_rds_db_creds import create_rds_db_credentials

@click.group()
def cli():
    """devops-auto - A cli tools for all the devops related tasks"""
    pass

@cli.command()
@click.option("--db-name", required=True, help="The name of the Database Hosted on AWS")
@click.option("--db-username", required=True, help="The username for the Database Hosted on AWS")
@click.option("--db-password", required=True, help="The password of the Database Hosted on AWS")
def create_db_creds(db_name: str, db_username: str, db_password: str):
    """Create Database Credentials"""
    create_rds_db_credentials(db_name, db_username, db_password)

if __name__ == "__main__":
    cli()