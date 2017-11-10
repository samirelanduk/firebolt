from unittest import TestCase
from unittest.mock import Mock, patch
from firebolt.http import Request, environ_to_request

class RequestCreationTests(TestCase):

	def test_can_create_request(self):
		request = Request("/path/to/resource/")
		self.assertEqual(request._uri, "/path/to/resource/")
		self.assertEqual(request._method, "GET")
		self.assertEqual(request._headers, {})


	def test_uri_must_be_str(self):
		with self.assertRaises(TypeError):
			Request(100)


	def test_can_create_request_with_method(self):
		request = Request("/path/to/resource/", method="POST")
		self.assertEqual(request._method, "POST")
		request = Request("/path/to/resource/", method="put")
		self.assertEqual(request._method, "PUT")


	def test_method_must_be_str(self):
		with self.assertRaises(TypeError):
			Request("/path/to/resource/", method=100)


	def test_can_create_request_with_headers(self):
		request = Request("/path/to/resource/", headers={"Host": "www.cat.com"})
		self.assertEqual(request._headers, {"Host": "www.cat.com"})



class RequestReprTests(TestCase):

	def test_request_repr(self):
		request = Request("/path/to/resource/", method="POST")
		self.assertEqual(str(request), "<POST Request: '/path/to/resource/'>")



class RequestIndexingTests(TestCase):

	def test_request_index_gets_headers(self):
		request = Request("/path/to/resource/", headers={"Host": "www.cat.com"})
		self.assertEqual(request["Host"], "www.cat.com")



class RequestIndexSettingTests(TestCase):

	def test_can_alter_headers(self):
		request = Request("/path/to/resource/", headers={"Host": "www.cat.com"})
		request["Host"] = "www.dog.com"
		self.assertEqual(request._headers, {"Host": "www.dog.com"})


	def test_can_make_headers(self):
		request = Request("/path/to/resource/", headers={"Host": "www.cat.com"})
		request["Accept"] = "text/plain"
		self.assertEqual(
		 request._headers, {"Host": "www.cat.com", "Accept": "text/plain"}
		)



class RequestUriTests(TestCase):

	def test_uri_property(self):
		request = Request("/path/to/resource/")
		self.assertIs(request._uri, request.uri)


	def test_can_update_uri(self):
		request = Request("/path/to/resource/")
		self.assertEqual(request._uri, "/path/to/resource/")
		request.uri = "/path2/"
		self.assertEqual(request._uri, "/path2/")


	def test_uri_must_be_str(self):
		request = Request("/path/to/resource/")
		with self.assertRaises(TypeError):
			request.uri = 1000



class RequestMethodTests(TestCase):

	def test_method_property(self):
		request = Request("/path/to/resource/")
		self.assertIs(request._method, request.method)


	def test_can_update_method(self):
		request = Request("/path/to/resource/")
		self.assertEqual(request.method, "GET")
		request.method = "POST"
		self.assertEqual(request._method, "POST")
		request.method = "delete"
		self.assertEqual(request._method, "DELETE")


	def test_method_must_be_str(self):
		request = Request("/path/to/resource/")
		with self.assertRaises(TypeError):
			request.method = 1000



class RequestHeadersTests(TestCase):

	def test_headers_property(self):
		request = Request("/path/to/resource/", headers={"Host": "www.cat.com"})
		self.assertEqual(request._headers, request.headers)
		self.assertIsNot(request._headers, request.headers)


	def test_headers_property_is_immutable(self):
		request = Request("/path/to/resource/", headers={"Host": "www.cat.com"})
		with self.assertRaises(AttributeError):
			request.headers = {}



class EnvironmentToRequestTests(TestCase):

	@patch("firebolt.http.Request")
	def test_can_get_request_from_envirnment(self, mock_request):
		mock_request.return_value = "REQUEST"
		environ = {
		 "REQUEST_METHOD": "POST",
		 "PATH_INFO": "/path/"
		}
		request = environ_to_request(environ)
		mock_request.assert_called_with("/path/", "POST")
		self.assertEqual(request, "REQUEST")
