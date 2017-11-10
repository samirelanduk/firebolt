"""The HTTP module - contains Request and Response functionality."""

class Request:
    """A HTTP Request. Headers are accessed via indexing.

    :param str uri: The URI of the request.
    :param str method: The HTTP method of the request. Will be converted to\
    upper case.
    :param dict headers: A ``dict`` of HTTP header field name and values.
    :raises TypeError: if the URI is not a string.
    :raises TypeError: if the method is not a string."""

    def __init__(self, uri, method="GET", headers=None):
        if not isinstance(uri, str):
            raise TypeError(("uri {} is not str".format(uri)))
        self._uri = uri
        if not isinstance(method, str):
            raise TypeError(("method {} is not str".format(method)))
        self._method = method.upper()
        self._headers = {} if headers is None else headers


    def __repr__(self):
        return "<{} Request: '{}'>".format(self._method, self._uri)


    def __getitem__(self, key):
        return self._headers[key]


    def __setitem__(self, key, value):
        self._headers[key] = value


    @property
    def uri(self):
        """The Uniform Resource Identifier - the string that points to the
        resource that the request is asking for. It must be a string.

        :rtype: ``str``"""

        return self._uri


    @uri.setter
    def uri(self, uri):
        if not isinstance(uri, str):
            raise TypeError(("uri {} is not str".format(uri)))
        self._uri = uri


    @property
    def method(self):
        """The HTTP method of the request. It must be a string, and will be\
        converted to upper case.

        :rtype: ``str``"""

        return self._method


    @method.setter
    def method(self, method):
        if not isinstance(method, str):
            raise TypeError(("method {} is not str".format(method)))
        self._method = method.upper()


    @property
    def headers(self):
        """The HTTP headers of the request, as a ``dict``

        :rtype: ``dict``"""

        return dict(self._headers)



class Response:
    """A HTTP Request. Headers are accessed via indexing.

    :param bytes body: The Response body.
    :param int status_code: The Response status code.
    :param str reason_phrase: The Response reason phrase.
    :param dict headers: The headers as key-value pairs.
    :raises TypeError: if the body is not bytes.
    :raises TypeError: if the status code is not int.
    :raises TypeError: if the reason phrase is not str.
    :raises ValueError: if the status code is not a valid HTTP status code."""

    def __init__(self, body, status_code=200, reason_phrase=None, headers=None):
        if not isinstance(body, bytes):
            raise TypeError("Response body {} is not bytes".format(body))
        if not isinstance(status_code, int):
            raise TypeError("Status code {} is not an int".format(status_code))
        if reason_phrase is not None and not isinstance(reason_phrase, str):
            raise TypeError("Phrase {} is not a string".format(reason_phrase))
        self._body = body
        self._status_code = status_code
        try:
            self._reason_phrase = Response.PHRASES[status_code]
        except KeyError:
            raise ValueError(
             "{} is not a valid HTTP Response status".format(status_code)
            )
        if reason_phrase:
            self._reason_phrase = reason_phrase
        self._headers = {} if headers is None else headers


    def __repr__(self):
        return "<Response ({})>".format(self._status_code)


    def __getitem__(self, key):
        return self._headers[key]


    def __setitem__(self, key, value):
        self._headers[key] = value


    @property
    def body(self):
        """The body of the HTTP response

        :rtype: ``bytes``"""

        return self._body


    @body.setter
    def body(self, body):
        if not isinstance(body, bytes):
            raise TypeError("Response body {} is not bytes".format(body))
        self._body = body


    @property
    def status_code(self):
        """The status code of the HTTP Response. Updating it will also update
        the reason_phrase.

        :rtype: ``int``"""

        return self._status_code


    @status_code.setter
    def status_code(self, status_code):
        if not isinstance(status_code, int):
            raise TypeError("Status code {} is not int".format(status_code))
        self._status_code = status_code
        try:
            self._reason_phrase = Response.PHRASES[status_code]
        except KeyError:
            raise ValueError(
             "{} is not a valid HTTP Response status".format(status_code)
            )


    @property
    def reason_phrase(self):
        """The short message describing the reason for the status code.

        :rtype: ``str``"""

        return self._reason_phrase


    @reason_phrase.setter
    def reason_phrase(self, reason_phrase):
        if not isinstance(reason_phrase, str):
            raise TypeError(("phrase {} is not str".format(reason_phrase)))
        self._reason_phrase = reason_phrase


    @property
    def headers(self):
        """The HTTP headers of the response, as a ``dict``

        :rtype: ``dict``"""

        return dict(self._headers)


    PHRASES = {
     100: "Continue", 101: "Switching Protocols", 200: "OK", 201: "Created",
     202: "Accepted", 203: "Non-Authoritative Information", 204: "No Content",
     205: "Reset Content", 206: "Partial Content", 207: "Multi-Status",
     226: "IM Used", 300: "Multiple Choices", 301: "Moved Permanently",
     302: "Found", 303: "See Other", 304: "Not Modified", 305: "Use Proxy",
     307: "Temporary Redirect", 400: "Bad Request", 401: "Unauthorized",
     402: "Payment Required", 403: "Forbidden", 404: "Not Found",
     405: "Method Not Allowed", 406: "Not Acceptable",
     407: "Proxy Authentication Required", 408: "Request Time-out",
     409: "Conflict", 410: "Gone", 411: "Length Required",
     412: "Precondition Failed", 413: "Request Entity Too Large",
     414: "Request-URI Too Large", 415: "Unsupported Media Type",
     416: "Requested range not satisfiable", 417: "Expectation Failed",
     418: "I'm a teapot", 422: "Unprocessable Entity", 423: "Locked",
     424: "Failed Dependency", 425: "Unordered Collection",
     426: "Upgrade Required", 444: "No Response", 449: "Retry With",
     450: "Blocked by Windows Parental Controls", 499: "Client Closed Request",
     500: "Internal Server Error", 501: "Not Implemented", 502: "Bad Gateway",
     503: "Service Unavailable", 504: "Gateway Time-out",
     505: "HTTP Version not supported", 506: "Variant Also Negotiates",
     507: "Insufficient Storage", 509: "Bandwidth Limit Exceeded",
     510: "Not Extended"
    }



def environ_to_request(environ):
    """Takes a WSGI environment ``dict`` and converts into a firebolt
    :py:class:`.Request`

    :param dict environ: The WSGI environment variables.
    :rtype: ``Request``"""

    request = Request(environ["PATH_INFO"], environ["REQUEST_METHOD"])
    return request
