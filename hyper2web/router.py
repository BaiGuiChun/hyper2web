import os

from .abstract import AbstractRouter
from .http import HTTP, Stream


class Router(AbstractRouter):
	"""User should never construct Router"""

	# todo: I may want to change the constructor
	def __init__(self, default_get):
		self._routes = {
			'GET': {},
			'POST': {}
		}
		self.default_get = default_get

	def register(self, method: str, route: str, handler):
		assert method in ['GET', 'POST']  # 这只是目前为了测试而加的限制
		self._routes[method][route] = handler

	def find_match(self, path: str):
		"""
		'user/{userId}' should match 'user/abc'
		userId = abc
		return a tuple (matched, parameters)
		matched is the route which matches the incoming path
		parameters is a dict of parameters and their values
		"""
		# todo: now the problem is how to implement it
		# todo: pattern matching should be independent from :method,
		# todo: but the current implementation doesn't support it. Should improve it later.
		print(self._routes.values())
		for routes_of_this_method in self._routes.values():
			print(routes_of_this_method)
			for route in routes_of_this_method:
				matched, parameters = self._match(route, path)
				if matched:
					return route, parameters
		return None, None

	@classmethod
	def _match(cls, route, path):
		# todo: it seems like that regular expression is not necessary
		# note: Could it be simpler? Could regex help?
		route = route.split('/')
		path = path.split('/')
		if len(route) != len(path):
			return False, None
		else:
			# todo: implement it
			parameters = {}
			for r, p in zip(route, path):
				if r[0] == '{' and r[-1] == '}':
					parameters[r[1:-1]] = p
				elif r != p:
					return False, None
			return True, parameters

	# async
	async def handle_route(self, http: HTTP, stream: Stream):
		print('app.App.handle_route')

		path = stream.headers[':path'].lstrip('/')
		method = stream.headers[':method']

		route, parameters = self.find_match(path)
		print('app.App.handle_route', route)

		# 如果没有任何匹配，就默认为静态文件读取
		if route is None:
			if method == 'GET':
				print('GET')
				handler = self.default_get
			else:
				handler = None
		else:
			handler = self._routes[method].get(route, None)

		if handler is not None:
			print('handle')
			print(handler)
			await handler(http, stream, parameters)
		else:
			# maybe raise an error?
			raise Exception(path, 'is not a valid request path')
