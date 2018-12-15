from unittest import TestCase

from set_symmetric_difference import find_sym_difference


class TestFindSymDifference(TestCase):
    def test_find_sym_difference(self):
        # self.fail()
        self.assertEqual({'c', 'e', 'H', 'n', 'R', 'r'},
                         find_sym_difference(set("Hacker"), set("Rank")), "sym diff failed")
