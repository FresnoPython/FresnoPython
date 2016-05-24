import datetime
import unittest
import webbrowser

try:
    # Python 3
    from unittest import mock
except ImportError:
    # Python 2
    import mock

import FresnoPython


class FresnoPythonTests(unittest.TestCase):
    @mock.patch('webbrowser.open', return_value=True)
    def _browser_test(self, func, wbo):
        ret = func()
        assert ret is True
        assert wbo.called
        assert wbo.call_count == 1

    def test_open_website(self):
        self._browser_test(FresnoPython.open_website)

    def test_open_map(self):
        self._browser_test(FresnoPython.open_map)

    def test_open_twitter(self):
        self._browser_test(FresnoPython.open_twitter)

    def test_next_meeting(self):
        date = datetime.date(2016, 5, 23)
        expected = datetime.datetime(2016, 5, 24, 18, 30)
        assert FresnoPython.next_meeting_date(date) == expected

    @mock.patch('webbrowser.open', return_val=True)
    def test_message(self, wbo):
        message = FresnoPython.message()

        # The message should contain info about Fresno.py
        assert FresnoPython.name in message
        assert FresnoPython.description in message
        assert FresnoPython.location in message
        assert FresnoPython.map in message
        assert FresnoPython.website in message
        assert FresnoPython.twitter in message
