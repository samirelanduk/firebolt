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
