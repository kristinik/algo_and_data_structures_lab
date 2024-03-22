import unittest
from src.sum_of_three import find_sum

class TestFindSum(unittest.TestCase):
    def test_find_sum_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        P = -9
        self.assertTrue(find_sum(arr, P))

    def test_find_sum_zero_P(self):
        arr = [1, 2, 3, 4, 5]
        P = 0
        self.assertFalse(find_sum(arr, P))

if __name__ == '__main__':
    unittest.main()
