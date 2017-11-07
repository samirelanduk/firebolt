from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from firebolt.wsgi import create_application

class WsgiTest(TestCase):

    def setUp(self):
        self.environ = {"header": "value"}
        self.callback = MagicMock()



class ApplicationCreationTests(WsgiTest):

    @patch("firebolt.wsgi.environ_to_request")
    def test_can_create_application(self, mock_request):
        app = create_application()
        self.assertFalse(mock_request.called)
        self.assertFalse(self.callback.called)
        app(self.environ, self.callback)
        mock_request.assert_called_with(self.environ)
        self.callback.assert_called_with(
         "200 OK", [('Content-type', 'text/plain; charset=utf-8')]
        )
