import unittest
from code import hello, create_num_list, custom_func_x, custom_non_lin_num_list


class TestHelloWorld(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), 'Hello World')

    def test_custom_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)

    def test_custom_func_x(self):
        self.assertEqual(custom_func_x(3, 2, 3), 54)

    def test_custom_non_lin_num_list(self):
        self.assertEqual(custom_non_lin_num_list(5, 2, 3)[2], 16)
        self.assertEqual(custom_non_lin_num_list(5, 3, 2)[4], 48)
