from .http import environ_to_request

def create_application(url_matcher):
    """Creates a WSGI application function.

    :rtype: ``func``"""

    def application(environment, start_response):
        request = environ_to_request(environment)
        responder = url_matcher(request.uri)
        start_response(
         "200 OK", [('Content-type', 'text/plain; charset=utf-8')]
        )
        if responder: return responder(request)
        return [b"404"]
    return application
