from unittest import TestCase
from unittest.mock import Mock, patch
from firebolt.http import Request

class RequestCreationTests(TestCase):

	def test_can_create_request(self):
		request = Request("/path/to/resource/")
		self.assertEqual(request._method, "GET")
		self.assertEqual(request._uri, "/path/to/resource/")


	def test_uri_must_be_str(self):
		with self.assertRaises(TypeError):
			request = Request(100)



class RequestUriTests(TestCase):

	def test_uri_property(self):
		request = Request("/path/to/resource/")
		self.assertIs(request._uri, request.uri)


	def test_can_update_uri(self):
		request = Request("/path/to/resource/")
		self.assertEqual(request.uri, "/path/to/resource/")
		request.uri = "/path2/"
		self.assertEqual(request._uri, "/path2/")


	def test_uri_must_be_str(self):
		request = Request("/path/to/resource/")
		with self.assertRaises(TypeError):
			request.uri = 1000