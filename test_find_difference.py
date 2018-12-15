from unittest import TestCase
from set_difference import find_difference


class TestFindDifference(TestCase):
    def test_find_difference(self):
        self.assertEqual(find_difference(), 1, "difference failed")
