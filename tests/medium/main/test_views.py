import unittest
import re
from flask import url_for
from celery import states as TASK_STATES
from celery.result import AsyncResult
from tests.base import TestCase


class IndexRouteTestCase(TestCase):
    ENDPOINT = 'main.index'

    def test_index_success(self):
        response = self.client.get(url_for(self.ENDPOINT))
        self.assertEqual(200, response.status_code)
        self.assertIn(b'welcome to CI/CD world', response.data)


class AddRouteTestCase(TestCase):
    ENDPOINT = 'main.add'

    def test_submit_add_job_success(self):
        response = self.client.get(url_for(self.ENDPOINT))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'submit add job success', response.data)

        task_id = re.match(b'submit add job success ([\\w\\-]*) ',
                           response.data).groups()[0]
        task = AsyncResult(task_id)
        task.get(timeout=10)
        self.assertEqual(TASK_STATES.SUCCESS, task.status)


if __name__ == '__main__':
    unittest.main()
