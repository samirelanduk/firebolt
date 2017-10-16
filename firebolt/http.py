"""The HTTP module - contains Request and Response functionality."""

class Request:

	def __init__(self, uri):
		if not isinstance(uri, str):
			raise TypeError(("uri {} is not str".format(uri)))
		self._uri = uri
		self._method = "GET"


	@property
	def uri(self):
		"""The Uniform Resource Identifier - the string that points to the
		resource that the request is asking for.

		:rtype: ``str``"""

		return self._uri


	@uri.setter
	def uri(self, uri):
		if not isinstance(uri, str):
			raise TypeError(("uri {} is not str".format(uri)))
		self._uri = uri