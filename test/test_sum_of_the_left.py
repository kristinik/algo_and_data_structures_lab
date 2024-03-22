import unittest
from src.sum_of_the_left import BinaryTree, Sums




class TestBranchSums(unittest.TestCase):
    def test_branch_sums(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)

        self.assertEqual(Sums(root), 24)

        self.assertEqual(Sums(None), 0)


if __name__ == '__main__':
    unittest.main()
