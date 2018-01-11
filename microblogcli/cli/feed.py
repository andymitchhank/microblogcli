import click
from bs4 import BeautifulSoup

from ..api import get_feed
from ..models import Account


@click.command()
@click.option('--limit', '-l', default=10)
def feed(limit):
	token = Account.current_token()
	posts = []

	for post in get_feed(token, limit):
		post_id = post['id']

		handle = f"@{post['author']['_microblog']['username']}"
		handle = click.style(handle, fg='green')

		content = BeautifulSoup(post['content_html'], "html.parser").get_text()

		posts.append('\n'.join([f'{handle} | {post_id}', content]))


	click.echo_via_pager('\n\n'.join(posts))








	

