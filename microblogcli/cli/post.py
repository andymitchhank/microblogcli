import click

from ..api import create_post
from ..models import Account


@click.command()
@click.option('--title', '-t', default=None)
@click.argument('content', required=False, default=None)
def post(title, content):
	""" Create a new post on your Micro.blog 

		This only works for hosted Micro.blog accounts for now. 
	"""
	if not content:
		content = click.prompt('', type=str)


	create_post(Account.current_token(), content, title)
	

