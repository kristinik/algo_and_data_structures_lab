class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def Sums(root):
    def help(node, is_right_child):

        if not node:
            return 0
        if not node.left and not node.right and is_right_child:

            return node.value
        return help(node.left, False) + help(node.right, True)


    return help(root, False)



