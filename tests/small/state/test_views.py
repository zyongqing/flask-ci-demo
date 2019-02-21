import unittest
from flask import url_for
from tests.base import TestCase


class ReadyRouteTestCase(TestCase):
    ENDPOINT = "state.ready"

    def test_ready_success(self):
        response = self.client.get(url_for(self.ENDPOINT))
        self.assertEqual(200, response.status_code)
        self.assertIn(b"yes", response.data)


if __name__ == "__main__":
    unittest.main()
