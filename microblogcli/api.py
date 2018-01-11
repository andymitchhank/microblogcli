from bessie import BaseClient, Endpoint

__all__ = ['create_post']

endpoints = {
	'POST': {
		'account/signin': None,
		'posts/favorites': None,
		'posts/reply': None,
		'users/follow': ['username'],
		'users/unfollow': ['username'],
		'micropub': ['h', 'content']
	},
	'GET': {
		'posts/all': None,
		'posts/mentions': None,
		'posts/favorites': None,
		'posts/<username>': None,
		'posts/conversation': ['id'],
		'posts/check': ['since_id'],
		'users/is_following': ['username'],
		'users/following/<username>': None
	},
	'DELETE': {
		'posts/favorites/<id>': None,
		'posts/<id>': None
	}
}

available_endpoints = [Endpoint(method, path, params) for method, paths in endpoints.items()
										   			  for path, params in paths.items()]


class PostingError(Exception): pass


class MicroBlogApi(BaseClient):

	endpoints = available_endpoints
	base_url='https://micro.blog'

	def __init__(self, path='', path_params=None, token=''):
		self.token = token
		super().__init__(path, path_params, token=token)

	# override method from BaseClient to inject Authorization header
	def _create_request(self):
		super()._create_request()
		self.request.headers['Authorization'] = 'Token {}'.format(self.token)


def create_post(token, content, title=None):
	mba = MicroBlogApi(token=token)

	payload = {
		'h': 'entry',
		'content': content
	}

	if title:
		payload['name'] = title

	r = mba.micropub.post(**payload)
	if r.status_code != 200:
		raise PostingError(r.text)


def get_feed(token, limit):
	mba = MicroBlogApi(token=token)

	payload = {}

	r = mba.posts.all.get(**payload)

	if r.status_code == 200:
		return r.json()['items']


def follow(token, username):
	mba = MicroBlogApi(token=token)

	payload = {
		'username': username
	}

	r = mba.users.follow.post(**payload)


def unfollow(token, username):
	mba = MicroBlogApi(token=token)

	payload = {
		'username': username
	}

	r = mba.users.unfollow.post(**payload)


def is_following(token, username):
	mba = MicroBlogApi(token=token)

	payload = {
		'username': username
	}

	r = mba.users.is_following.get(**payload)

	return r.json()['is_following']


def following(token, username):
	mba = MicroBlogApi(token=token)

	r = mba.users.following.username(username).get()

	return r.json()