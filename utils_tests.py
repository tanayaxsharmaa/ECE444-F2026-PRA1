import unittest

from utils import utils


class TestReversed(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(utils.reversed(123), 321)
        self.assertEqual(utils.reversed(1200), 21)
        self.assertEqual(utils.reversed(-456), -654)
        self.assertEqual(utils.reversed(7), 7)
        self.assertEqual(utils.reversed(0), 0)

    def test_strings(self):
        with self.assertRaises(TypeError):
            utils.reversed("123")
        with self.assertRaises(TypeError):
            utils.reversed("abc")

    def test_floats(self):
        with self.assertRaises(ValueError):
            utils.reversed(12.5)
        with self.assertRaises(ValueError):
            utils.reversed(-3.0)


class TestFormatter(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(utils.formatter(10), ("1010", "12"))
        self.assertEqual(utils.formatter(0), ("0", "0"))
        self.assertEqual(utils.formatter(64), ("1000000", "100"))
        self.assertEqual(utils.formatter(-10), ("-1010", "-12"))

    def test_strings(self):
        with self.assertRaises(ValueError):
            utils.formatter("10")
        with self.assertRaises(ValueError):
            utils.formatter("abc")

    def test_floats(self):
        with self.assertRaises(ValueError):
            utils.formatter(10.5)
        with self.assertRaises(ValueError):
            utils.formatter(8.0)


if __name__ == "__main__":
    unittest.main()
