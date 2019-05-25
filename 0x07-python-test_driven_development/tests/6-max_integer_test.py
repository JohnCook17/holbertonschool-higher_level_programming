#!/urs/bin/python3
"""
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_int(self):
        self.assertIsInstance(1, int)
