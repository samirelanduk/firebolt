from unittest import TestCase
from unittest.mock import Mock, patch
from firebolt.http import Response

class ResponseCreationTests(TestCase):

    def test_can_create_response(self):
        response = Response(b"<html>Hello</html>")
        self.assertEqual(response._body, b"<html>Hello</html>")
        self.assertEqual(response._status_code, 200)
        self.assertEqual(response._reason_phrase, "OK")
        self.assertEqual(response._headers, {})


    def test_body_must_be_bytes(self):
        with self.assertRaises(TypeError):
            Response("<html>Hello</html>")


    def test_can_create_response_with_status_code(self):
        response = Response(b"<html>Hello</html>", status_code=404)
        self.assertEqual(response._body, b"<html>Hello</html>")
        self.assertEqual(response._status_code, 404)
        self.assertEqual(response._reason_phrase, "Not Found")
        self.assertEqual(response._headers, {})


    def test_status_code_must_be_integer(self):
        with self.assertRaises(TypeError):
            Response(b"<html>Hello</html>", status_code="404")


    def test_status_code_must_be_valid(self):
        with self.assertRaises(ValueError):
            Response(b"<html>Hello</html>", status_code=600)


    def test_can_create_response_with_reason_phrase(self):
        response = Response(b"<html>Hello</html>", reason_phrase="Splendid")
        self.assertEqual(response._body, b"<html>Hello</html>")
        self.assertEqual(response._status_code, 200)
        self.assertEqual(response._reason_phrase, "Splendid")
        self.assertEqual(response._headers, {})


    def test_reason_phrase_must_be_str(self):
        with self.assertRaises(TypeError):
            Response(b"<html>Hello</html>", reason_phrase=1.1)


    def test_can_create_response_with_headers(self):
        response = Response(b"<html>Hello</html>", headers={"Content-Length": "348"})
        self.assertEqual(response._headers, {"Content-Length": "348"})



class ResponseReprTests(TestCase):

    def test_response_repr(self):
        response = Response(b"<html>Hello</html>")
        self.assertEqual(str(response), "<Response (200)>")



class ResponseIndexingTests(TestCase):

	def test_request_index_gets_headers(self):
		response = Response(b"<html>Hello</html>", headers={"Content-Length": "348"})
		self.assertEqual(response["Content-Length"], "348")



class RequestIndexSettingTests(TestCase):

	def test_can_alter_headers(self):
		response = Response(b"<html>Hello</html>", headers={"Content-Length": "348"})
		response["Content-Length"] = "101"
		self.assertEqual(response._headers, {"Content-Length": "101"})


	def test_can_make_headers(self):
		response = Response(b"<html>Hello</html>", headers={"Content-Length": "348"})
		response["Vary"] = "Accept-Language"
		self.assertEqual(
		 response._headers, {"Content-Length": "348", "Vary": "Accept-Language"}
		)



class ResponseBodyTests(TestCase):

    def test_body_property(self):
        response = Response(b"<html>Hello</html>")
        self.assertIs(response._body, response.body)


    def test_can_update_body(self):
        response = Response(b"<html>Hello</html>")
        self.assertEqual(response._body, b"<html>Hello</html>")
        response.body = b"<html>Ho</html>"
        self.assertEqual(response._body, b"<html>Ho</html>")


    def test_body_must_be_bytes(self):
        response = Response(b"<html>Hello</html>")
        with self.assertRaises(TypeError):
            response.body = "Hi"



class ResponseStatusCodeTests(TestCase):

    def test_status_code_property(self):
        response = Response(b"<html>Hello</html>")
        self.assertIs(response._status_code, response.status_code)


    def test_can_update_status_code(self):
        response = Response(b"<html>Hello</html>")
        self.assertEqual(response._status_code, 200)
        response.status_code = 404
        self.assertEqual(response._status_code, 404)
        self.assertEqual(response._reason_phrase, "Not Found")


    def test_status_code_must_be_int(self):
        response = Response(b"<html>Hello</html>")
        with self.assertRaises(TypeError):
            response.status_code = "100"


    def test_status_code_must_be_valid(self):
        response = Response(b"<html>Hello</html>")
        with self.assertRaises(ValueError):
            response.status_code = 600



class ResponseReasonPhraseTests(TestCase):

    def test_reason_phrase_property(self):
        response = Response(b"<html>Hello</html>")
        self.assertIs(response._reason_phrase, response.reason_phrase)


    def test_can_update_reason_phrase(self):
        response = Response(b"<html>Hello</html>")
        self.assertEqual(response._reason_phrase, "OK")
        response.reason_phrase = "Bad"
        self.assertEqual(response._reason_phrase, "Bad")


    def test_reason_phrase_must_be_str(self):
        response = Response(b"<html>Hello</html>")
        with self.assertRaises(TypeError):
            response.reason_phrase = 1000



class ResponseHeadersTests(TestCase):

	def test_headers_property(self):
		response = Response(b"<html>Hello</html>", headers={"Content-Length": "348"})
		self.assertEqual(response._headers, response.headers)
		self.assertIsNot(response._headers, response.headers)


	def test_headers_property_is_immutable(self):
		response = Response(b"<html>Hello</html>", headers={"Content-Length": "348"})
		with self.assertRaises(AttributeError):
			response.headers = {}
