import unittest
from proj1controller import *


class TestProj1Controller(unittest.TestCase):

    def test_one(self):
        with self.assertRaises(ValueError):
            one(-3)
            one(0)
        with self.assertRaises(TypeError):
            one('2')
            one(1.5)

    def test_two(self):
        with self.assertRaises(ValueError):
            two(2, -3)
        with self.assertRaises(TypeError):
            two('2', 2)
            two(2, '2')
            two('2', '2')

    def test_three(self):
        with self.assertRaises(ValueError):
            three(-3)
            three(0)
        with self.assertRaises(TypeError):
            three('2')
            three(1.5)


if __name__ == '__main__':
    unittest.main()