class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def Sums(root):
    def helper(node, is_left_child):
    def helper(node, is_right_child)    
        if not node:
            return 0
        if not node.left and not node.right and is_left_child:
        if not node.left and not node.right and is_right_child:    

            return node.value
        return helper(node.left, True) + helper(node.right, False)
        return helper(node.left, False) + helper(node.right, True)

    return helper(root, False)


root = BinaryTree(4)
root.left = BinaryTree(11)
root.right = BinaryTree(21)
root.right.left = BinaryTree(17)
root.right.right = BinaryTree(6)


print(Sums(root))
