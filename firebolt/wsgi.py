from .http import environ_to_request

def create_application(url_matcher):
    """Creates a WSGI application function.

    :rtype: ``func``"""

    def application(environment, start_response):
        request = environ_to_request(environment)
        responder = url_matcher(request.uri)
        if responder:
            response = responder(request)
            start_response(
             "{} {}".format(response.status_code, response.reason_phrase),
             [(key, response.headers[key]) for key in response.headers]
            )
            return response.body.split(b"\n")
        else:
            start_response("200 OK", [('Content-type', 'text/html; charset=utf-8')])
            return [b"Hi"]

    return application
