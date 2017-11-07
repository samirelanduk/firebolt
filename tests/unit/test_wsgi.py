from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from firebolt.wsgi import create_application

class WsgiTest(TestCase):

    def setUp(self):
        self.environ = {"header": "value"}
        self.callback = MagicMock()
        self.matcher = MagicMock()



class ApplicationCreationTests(WsgiTest):

    @patch("firebolt.wsgi.environ_to_request")
    def test_can_create_application(self, mock_request):
        request = Mock()
        request.uri = "/1/2/3/"
        mock_request.return_value = request
        app = create_application(self.matcher)
        self.assertFalse(mock_request.called)
        self.assertFalse(self.callback.called)
        self.assertFalse(self.matcher.called)
        app(self.environ, self.callback)
        mock_request.assert_called_with(self.environ)
        self.callback.assert_called_with(
         "200 OK", [('Content-type', 'text/plain; charset=utf-8')]
        )
        self.matcher.assert_called_with("/1/2/3/")
