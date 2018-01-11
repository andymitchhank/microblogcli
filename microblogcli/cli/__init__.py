import click
from click import echo

from ..models import create_tables
from .account import account
from .post import post
from .feed import feed
from .users import follow, unfollow, following, am_following


create_tables()


@click.group()
def cli():
    pass


cli.add_command(account)
cli.add_command(post)
cli.add_command(feed)
cli.add_command(follow)
cli.add_command(unfollow)
cli.add_command(following)
cli.add_command(am_following)
