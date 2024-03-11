import unittest
from src.leaves_sum import BinaryTree, Sums


class TestBranchSums(unittest.TestCase):
    def test_branch_sums(self):

        root = BinaryTree(4)
        root.left = BinaryTree(11)
        root.right = BinaryTree(21)
        root.right.left = BinaryTree(17)
        root.right.right = BinaryTree(6)


        self.assertEqual(Sums(root), 28)


        self.assertEqual(Sums(None), 0)

if __name__ == '__main__':
    unittest.main()