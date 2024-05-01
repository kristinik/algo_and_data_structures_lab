import unittest
from src.Rabin_Karp import *


class TestRabinKarp(unittest.TestCase):
    def test_no_match(self):
        haystack = "abcdefg"
        needle = "xyz"
        self.assertEqual(rabin_karp(haystack, needle), [])

    def test_basic(self):
        haystack = "ababcababcabc"
        needle = "abc"
        expected = [2, 7, 10]
        self.assertEqual(rabin_karp(haystack, needle), expected)

    def test_empty_input(self):
        haystack = ""
        needle = "abc"
        self.assertEqual(rabin_karp(haystack, needle), [])

        haystack = "abc"
        needle = ""
        self.assertEqual(rabin_karp(haystack, needle), [])

    def test_same_strings(self):
        haystack = "abc"
        needle = "abc"
        expected = [0]
        self.assertEqual(rabin_karp(haystack, needle), expected)

    def test_edge_case(self):
        haystack = "aaaaa"
        needle = "aa"
        self.assertEqual(rabin_karp(haystack, needle), [0, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()