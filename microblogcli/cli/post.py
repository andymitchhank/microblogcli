import click

from ..api import create_post
from ..models import Account


@click.command()
@click.option('--title', '-t', default=None)
@click.argument('content')
def post(title, content):
	""" Create a new post on your Micro.blog 

		This only works for hosted Micro.blog accounts for now. 
	"""

	create_post(Account.current_token(), content, title)
	

