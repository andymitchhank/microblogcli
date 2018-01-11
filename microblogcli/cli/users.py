import click

from ..models import Account
from .. import api

@click.command()
@click.argument('username')
def follow(username):
	token = Account.current_token()
	api.follow(token, username)

@click.command()
@click.argument('username')
def unfollow(username):
	token = Account.current_token()
	api.unfollow(token, username)


@click.command()
@click.argument('username')
def am_following(username):
	token = Account.current_token()
	click.echo(api.is_following(token, username))


@click.command()
@click.argument('username', required=False)
def following(username=None):
	token = Account.current_token()

	if not username:
		username = Account.current_username()

	users = '\n'.join(f"{u['name']} (@{u['username']})" for u in api.following(token, username))
	click.echo(users)



