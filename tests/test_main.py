import unittest
from flask import url_for
from tests.base import TestCase
from app.blueprints.main.views import task_add


class MainTestCase(TestCase):

    def test_index_success(self):
        response = self.client.get(url_for('main.index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'hello world')

    def test_index_failed(self):
        response = self.client.get('undefined_page')
        self.assertEqual(response.status_code, 404)

    def test_add_success(self):
        response = self.client.get(url_for('main.add'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'add job submit')

    def test_add_job_success(self):
        x, y = 98, 99
        result = task_add(x, y)
        self.assertEqual(result, x+y)


if __name__ == '__main__':
    unittest.main()
