import unittest
from flask import url_for
from tests.base import TestCase


class MainTestCase(TestCase):

    def test_index_success(self):
        response = self.client.get(url_for('main.index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'hello world')

    def test_index_failed(self):
        response = self.client.get('undefined_page')
        self.assertEqual(response.status_code, 500)


if __name__ == '__main__':
    unittest.main()
