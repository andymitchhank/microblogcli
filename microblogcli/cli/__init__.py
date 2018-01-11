import click
from click import echo

from ..models import create_tables
from .account import account


create_tables()


@click.group()
def cli():
    pass


cli.add_command(account)

