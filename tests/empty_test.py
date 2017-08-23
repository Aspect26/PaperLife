import unittest


class TestAlwaysTrue(unittest.TestCase):

    def test_true(self):
        self.assertEqual(True, True, "True shall be always equal to True")
