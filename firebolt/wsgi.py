from .http import environ_to_request

def create_application():
    """Creates a WSGI application function.

    :rtype: ``func``"""

    def application(environment, start_response):
        request = environ_to_request(environment)
        start_response(
         "200 OK", [('Content-type', 'text/plain; charset=utf-8')]
        )
        return [b"Hello, world!"]
    return application
