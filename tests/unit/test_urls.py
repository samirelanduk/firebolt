from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from firebolt.urls import UrlMatcher

class UrlTest(TestCase):

    def setUp(self):
        self.responder1 = lambda r: None
        self.responder2 = lambda r: None



class UrlMatcherCreationTests(UrlTest):

    def test_can_create_matcher(self):
        matcher = UrlMatcher(
         (r"/", self.responder1), (r"/about/", self.responder2)
        )
        self.assertEqual(matcher._lookup, [
         (r"/", self.responder1), (r"/about/", self.responder2)
        ])


    def test_url_matcher_needs_iterables_len_2(self):
        with self.assertRaises(ValueError):
            UrlMatcher(
             (r"/", self.responder1), (r"/about/", self.responder2, 5)
            )


    def test_url_matcher_needs_strings(self):
        with self.assertRaises(TypeError):
            UrlMatcher(
             (r"/", self.responder1), (100, self.responder2)
            )



class UrlMatcherReprTests(UrlTest):

    def test_url_matcher_repr(self):
        matcher = UrlMatcher(
         (r"/", self.responder1), (r"/about/", self.responder2)
        )
        self.assertEqual(str(matcher), "<UrlMatcher (patterns: 2)>")



class UrlMatchingTests(UrlTest):

    def test_can_get_responder_by_string(self):
        matcher = UrlMatcher(
         (r"/help/", self.responder1), (r"/about/", self.responder2)
        )
        self.assertIs(matcher("/help/"), self.responder1)
        self.assertIs(matcher("/about/"), self.responder2)
        self.assertIsNone(matcher("/halp/"))


    def test_can_get_responder_by_regex(self):
        matcher = UrlMatcher(
         (r"/(.+?)/edit/", self.responder1), (r"/about/(\d+)/", self.responder2)
        )
        self.assertIs(matcher("/blob/edit/"), self.responder1)
        self.assertIs(matcher("/about/45/"), self.responder2)
        self.assertIsNone(matcher("/help/ss/"))
