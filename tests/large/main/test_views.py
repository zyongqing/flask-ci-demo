import unittest
import requests
from tests.base import TestCase
from tests.large.helper import url_for


class IndexRouteTestCase(TestCase):
    ENDPOINT = "main.index"

    def test_index_success(self):
        response = requests.get(url_for(self.ENDPOINT))
        self.assertEqual(200, response.status_code)
        self.assertIn("welcome to CI/CD world", response.text)


class AddRouteTestCase(TestCase):
    ENDPOINT = "main.add"

    def test_submit_add_job_success(self):
        response = requests.get(url_for(self.ENDPOINT))
        self.assertEqual(200, response.status_code)
        self.assertIn("submit add job success", response.text)


if __name__ == "__main__":
    unittest.main()
