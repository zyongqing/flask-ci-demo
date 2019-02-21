import unittest
import requests
from tests.base import TestCase
from tests.large.helper import url_for


class ReadyRouteTestCase(TestCase):
    ENDPOINT = "state.ready"

    def test_ready_success(self):
        response = requests.get(url_for(self.ENDPOINT))
        self.assertEqual(200, response.status_code)
        self.assertIn("yes", response.text)


if __name__ == "__main__":
    unittest.main()
