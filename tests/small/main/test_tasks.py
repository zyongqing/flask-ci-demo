import unittest
from tests.base import TestCase
from app.blueprints.main.tasks import add


class AddTaskTestCase(TestCase):
    def test_add_int_number_success(self):
        x, y, expect = 98, 99, 197
        result = add(x, y)
        self.assertEqual(result, expect)

    def test_add_float_number_success(self):
        x, y, expect = 98.5, 99.5, 198
        result = add(x, y)
        self.assertEqual(result, expect)

    def test_add_str_number_failed(self):
        x, y = "98", "99"
        with self.assertRaises(Exception):
            add(x, y)


if __name__ == "__main__":
    unittest.main()
