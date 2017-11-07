

class UrlMatcher:
    """A URL matcher takes a URL and returns a responder, using a lookup table.

    :param urls: The URL patterns to use as lookup.
    :raises TypeError: if the first item in each URL isn't a string.
    :raises ValueError: if any of the URLs aren't two-tuples."""

    def __init__(self, *urls):
        for url in urls:
            if len(url) != 2:
                raise ValueError(
                 "A URL pattern is an iterable of length 2, not {}".format(url)
                )
            if not isinstance(url[0], str):
                raise TypeError(
                 "{} is not a string or regex pattern".format(url[0])
                )
        self._lookup = list(urls)


    def __repr__(self):
        return "<UrlMatcher (patterns: {})>".format(len(self._lookup))
