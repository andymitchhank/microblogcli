from bessie import BaseClient, Endpoint

__all__ = ['create_post']

endpoints = {
	'POST': {
		'account/signin': None,
		'posts/favorites': None,
		'posts/reply': None,
		'users/follow': None,
		'users/unfollow': None,
		'micropub': None
	},
	'GET': {
		'posts/all': None,
		'posts/mentions': None,
		'posts/favorites': None,
		'posts/<username>': None,
		'posts/conversation': ['id'],
		'posts/check': ['since_id']
	},
	'DELETE': {
		'posts/favorites/<id>': None,
		'posts/<id>': None
	}
}

available_endpoints = [Endpoint(method, path, params) for method, paths in endpoints.items()
										   			  for path, params in paths.items()]


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
