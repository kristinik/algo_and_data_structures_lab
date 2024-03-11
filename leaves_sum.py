class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def Sums(root):
    def helper(node, is_left_child):
        if not node:
            return 0
        if not node.left and not node.right and is_left_child:
            return node.value
        return helper(node.left, True) + helper(node.right, False)

    return helper(root, False)


root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.right.left = BinaryTree(15)
root.right.right = BinaryTree(7)


print(Sums(root))