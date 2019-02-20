import unittest
import uuid
from unittest import mock
from flask import url_for
from tests.base import TestCase


class IndexRouteTestCase(TestCase):
    ENDPOINT = "main.index"

    def test_index_success(self):
        response = self.client.get(url_for(self.ENDPOINT))
        self.assertEqual(200, response.status_code)
        self.assertIn(b"welcome to CI/CD world", response.data)


class AddRouteTestCase(TestCase):
    ENDPOINT = "main.add"

    @mock.patch("app.blueprints.main.views.task_add")
    def test_submit_add_job_success(self, task_add):
        task_id = uuid.uuid1()
        task_add.delay = mock.Mock(return_value=task_id)
        response = self.client.get(url_for(self.ENDPOINT))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"submit add job success", response.data)

    @mock.patch("app.blueprints.main.views.task_add")
    def test_submit_add_job_failed(self, task_add):
        task_add.delay = mock.Mock(side_effect=Exception("Oops"))
        response = self.client.get(url_for(self.ENDPOINT))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"submit add job failed", response.data)


if __name__ == "__main__":
    unittest.main()
