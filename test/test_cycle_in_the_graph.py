import unittest
from src.cycle_in_the_graph import *

class TestHasCycle(unittest.TestCase):
    def test_graph_with_cycle(self):
        graph_with_cycle = {
            1: [2, 3, 4],
            2: [1, 5, 6],
            3: [1],
            4: [1, 7, 8],
            5: [2, 6, 9, 10],
            6: [2, 5, 10],
            7: [4, 8, 11, 12],
            8: [4, 7],
            9: [5],
            10: [5, 6],
            11: [7],
            12: [7]
        }
        self.assertTrue(has_cycle(graph_with_cycle), "Помилка: Очікувався цикл, але функція не повернула True")

    def test_graph_without_cycle(self):
        graph_without_cycle = {
            1: [2, 3, 4],
            2: [1, 5],
            3: [1],
            4: [1, 7, 8],
            5: [2, 6],
            6: [5, 10],
            7: [4, 8],
            8: [4, 7],
            9: [5],
            10: [6]
        }
        self.assertTrue(has_cycle(graph_without_cycle), "Помилка: Граф не має циклу, але функція повернула False")


if __name__ == '__main__':
    unittest.main()