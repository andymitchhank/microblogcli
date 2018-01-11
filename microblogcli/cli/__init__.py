import click
from click import echo

from ..models import create_tables
from .account import account
from .post import post


create_tables()


@click.group()
def cli():
    pass


cli.add_command(account)
cli.add_command(post)
