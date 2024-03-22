import unittest
from src.pumkins import find_sum

class TestFindSum(unittest.TestCase):
    def test_find_sum_even_rows(self):
        our_list = [[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]]
        expected_result = [1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12, 16, 15, 14, 13]
        self.assertEqual(find_sum(our_list), expected_result)

    def test_find_sum_odd_rows(self):
        our_list = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12]]
        expected_result = [1, 2, 3, 6, 5, 4, 7, 8, 9, 12, 11, 10]
        self.assertEqual(find_sum(our_list), expected_result)

    def test_find_sum_empty_list(self):
        our_list = []
        expected_result = []
        self.assertEqual(find_sum(our_list), expected_result)

if __name__ == '__main__':
    unittest.main()
