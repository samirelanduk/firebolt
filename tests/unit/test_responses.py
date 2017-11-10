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
