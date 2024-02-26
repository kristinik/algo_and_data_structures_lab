import unittest
from lab1 import robot

class TestRobot(unittest.TestCase):

    def test_5x5(self):
        our_list = [[1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20],
                    [21, 22, 23, 24, 25]]
        expected_output = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15, 20, 19, 18, 17, 16, 21, 22, 23, 24, 25]
        self.assertEqual(robot(our_list), expected_output)

    def test_2x4(self):
        our_list = [[1, 2, 3, 4],
                    [5, 6, 7, 8]]
        expected_output = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(robot(our_list), expected_output)

    def test_1x1(self):
        our_list = [[1]]
        expected_output = [1]
        self.assertEqual(robot(our_list), expected_output)

    def test_6x1(self):
        our_list = [[1], [2], [3], [4], [5], [6]]
        expected_output = [1, 2, 3, 4, 5, 6]
        self.assertEqual(robot(our_list), expected_output)


if __name__ == '__main__':
    unittest.main()


