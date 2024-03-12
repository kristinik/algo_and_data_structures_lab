import unittest
from lab2 import find_sum



class Test(unittest.TestCase):
    def test_find_three_elements_positive(self):
      self.assertTrue(find_sum([1, 1, 1], 3))
      self.assertTrue(find_sum([1000000000, 1000000000, 1000000000], 3000000000))

    def test_find_three_elements_negative(self):
       self.assertFalse(find_sum([1, 2, 3, 10], 10))
       self.assertFalse(find_sum([1, 1, 1], 10))

    def test_find_three_elements_boundary(self):
        self.assertTrue(find_sum([1, 2, 3], 6))
        self.assertTrue(find_sum([999999999, 999999999, 999999999], 2999999997))


if __name__ == '__main__':
    unittest.main()



