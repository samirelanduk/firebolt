"""The HTTP module - contains Request and Response functionality."""

class Request:
	"""A HTTP Request.

	:param str uri: The URI of the request.
	:param str method: The HTTP method of the request. Will be converted to\
	upper case.
	:param dict headers: A ``dict`` of HTTP header field name and values.
	:raises TypeError: if the URI is not a string.
	:raises TypeError: if the method is not a string."""

	def __init__(self, uri, method="GET", headers=None):
		if not isinstance(uri, str):
			raise TypeError(("uri {} is not str".format(uri)))
		self._uri = uri
		if not isinstance(method, str):
			raise TypeError(("method {} is not str".format(method)))
		self._method = method.upper()
		self._headers = {} if headers is None else headers


	@property
	def uri(self):
		"""The Uniform Resource Identifier - the string that points to the
		resource that the request is asking for. It must be a string.

		:rtype: ``str``"""

		return self._uri


	@uri.setter
	def uri(self, uri):
		if not isinstance(uri, str):
			raise TypeError(("uri {} is not str".format(uri)))
		self._uri = uri


	@property
	def method(self):
		"""The HTTP method of the request. It must be a string, and will be\
		converted to upper case.

		:rtype: ``str``"""

		return self._method


	@method.setter
	def method(self, method):
		if not isinstance(method, str):
			raise TypeError(("method {} is not str".format(method)))
		self._method = method.upper()


	@property
	def headers(self):
		"""The HTTP headers of the request, as a ``dict``

		:rtype: ``dict``"""
		
		return dict(self._headers)