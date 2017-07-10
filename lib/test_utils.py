import unittest
import utils
import sys

test_strings = [
    "@chris you around?",
    "Good morning! (megusta) (coffee)",
    "Olympics are starting soon; http://www.nbcolympics.com",
    "@bob @john (success) such a cool feature; https://twitter.com/jdorfman/status/430511497475670016",
]


class TestParseMentions(unittest.TestCase):

    def test_case_1(self):
        ans = []
        for inp in test_strings:
            ans.append(utils.parse_mentions(inp))
        self.assertEqual(
            [['chris'], None, None, ['bob', 'john']], ans
        )


class TestParseEmoticons(unittest.TestCase):

    def test_case_1(self):
        ans = []
        for inp in test_strings:
            ans.append(utils.parse_emoticons(inp))
        self.assertEqual(
            [None, ['megusta', 'coffee'], None, ['success']], ans
        )


class TestParseLinks(unittest.TestCase):

    def test_case_1(self):
        ans = []
        for inp in test_strings:
            ans.append(utils.parse_links(inp))
        self.assertEqual(
            [None, None,[{'url': 'http://www.nbcolympics.com', 'title': '2018 PyeongChang Olympic Games | NBC Olympics'}], [{'url': 'https://twitter.com/jdorfman/status/430511497475670016', 'title': 'Justin Dorfman; on Twitter: "nice @littlebigdetail from @HipChat (shows hex colors when pasted in chat). http://t.co/7cI6Gjy5pq"'}]], ans
        )
