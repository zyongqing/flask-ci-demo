import unittest
from flask import url_for
from tests.base import TestCase


class MainTestCase(TestCase):

    def test_index_success(self):
        response = self.client.get(url_for('main.index'))
        self.assertTrue(response.status_code, 200)
        self.assertTrue(response.data, 'hello world')


if __name__ == '__main__':
    unittest.main()
