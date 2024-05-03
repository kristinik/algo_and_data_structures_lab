import unittest
from src.islands import *

class TestGraphAlgorithms(unittest.TestCase):
    def test_kruskal_mst(self):
        graph = [
            [0, 1, 2, 3],
            [1, 0, 0, 4],
            [2, 0, 0, 5],
            [3, 4, 5, 0]
        ]
        expected_weight = 6
        actual_weight = kruskal_mst(graph)
        self.assertEqual(actual_weight, expected_weight)


def test_read_empty_graph(self):
        start, finish, graph_data = read_graph('../resources/islands_empty.csv')
        self.assertEqual(start, None)
        self.assertEqual(finish, None)
        self.assertEqual(graph_data, {})

if __name__ == '__main__':
    unittest.main()