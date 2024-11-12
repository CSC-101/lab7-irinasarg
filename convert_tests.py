import unittest
import convert

class TestCases(unittest.TestCase):

    def test_str_to_float_1(self):
        self.assertEqual(convert.str_to_float("100.5"), 100.5)

    def test_str_to_float_2(self):
        self.assertIsNone(convert.str_to_float("hello"))


if __name__ == "__main__":
    unittest.main()