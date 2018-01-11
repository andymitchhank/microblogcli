import click
from tabulate import tabulate

from ..models import Account
from .utils import format_with_suggestion


@click.group()
def account():
	pass


@account.command()
@click.argument('username')
@click.option('--token', prompt=True, hide_input=True, confirmation_prompt=True)
def add(username, token):
	""" Add a new Micro.blog account """

	if Account.exists(username):
		click.echo(format_with_suggestion(f'{username} already exists. To update an account use ', '$ microblog account update <username>'))
		return

	a = Account(username=username, token=token)

	if Account.count() == 0:
		a.is_current = True

	a.save()

	click.echo(format_with_suggestion(f'{username} added! To list all accounts use ', '$ microblog account list'))


@account.command()
@click.argument('username')
@click.option('--token', prompt=True, hide_input=True, confirmation_prompt=True)
def update(username, token):
	""" Update an account with a new token """

	if not Account.exists(username):
		click.echo(f'{username} does not exists.')
		return

	Account.set_token(username, token)

	click.echo(f'{username} updated! To list all accounts use ')


@account.command()
def list():
	""" List all accounts """

	accounts = [[a.username, click.style('current', fg='blue')] if a.is_current else [a.username, ''] for a in Account.select()]
	click.echo(tabulate(accounts, tablefmt="plain"))


@account.command()
@click.argument('username')
def switch(username):
	""" Switch accounts given a username """ 

	if not Account.exists(username):
		click.echo(f'{username} does not exists.')
		return

	Account.clear_current()
	Account.set_current(username)

	click.echo(format_with_suggestion(f'{username} set as current. To view feed use ', '$ microblog feed'))


