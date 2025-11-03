#!/usr/bin/env python3

import click
from cli.create_rds_db_creds import create_rds_db_credentials

@click.group()
def cli():
    """devops-auto - A cli tools for all the devops related tasks"""
    pass

@cli.command()
@click.option("--dbname", required=True, help="The name of the Database Hosted on AWS")
def create_db_creds(dbname: str):
    """Create Database Credentials"""
    create_rds_db_credentials(dbname)

if __name__ == "__main__":
    cli()