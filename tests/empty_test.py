import unittest


class AlwaysTrueTest(unittest.TestCase):

    def testTrue(self):
        self.assertEqual(True, True, "True shall be always equal to True")
