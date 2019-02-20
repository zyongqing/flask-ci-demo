import os
import unittest
import requests
from requests.compat import urljoin
from flask import url_for
from tests.base import TestCase

WEB_DOMAIN = os.getenv("WEB_DOMAIN", "web")


def get_url(endpoint):
    return urljoin("http://{}".format(WEB_DOMAIN), url_for(endpoint))


class IndexRouteTestCase(TestCase):
    ENDPOINT = "main.index"

    def test_index_success(self):
        response = requests.get(get_url(self.ENDPOINT))
        self.assertEqual(200, response.status_code)
        self.assertIn("welcome to CI/CD world", response.text)


class AddRouteTestCase(TestCase):
    ENDPOINT = "main.add"

    def test_submit_add_job_success(self):
        response = requests.get(get_url(self.ENDPOINT))
        self.assertEqual(200, response.status_code)
        self.assertIn("submit add job success", response.text)


if __name__ == "__main__":
    unittest.main()
