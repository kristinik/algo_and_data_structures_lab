class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def Sums(root):
    def help(node, is_left_child):

        if not node:
            return 0
        if not node.left and not node.right and is_left_child:

            return node.value
        return help(node.left, True) + help(node.right, False)


    return help(root, False)



