# Given a binary search tree, return the minimum difference between any two nodes in the tree.

# Ex: Given the following tree...
#         2
#        / \
#       3   1
# return 1.

# Ex: Given the following tree...
#         29
#        /  \
#      17   50
#     /     / \
#    1    42  59
# return 8.

# Ex: Given the following tree...
#         2
#          \
#          100
# return 98.
class BinaryTree:
    def __init__(self):
        self.root = None

    def addNode(self, value):
        def traverse(node, value):
            if not node:
                node = TreeNode(value)
                return node
            if node.value > value:
                node.leftChild = traverse(node.leftChild, value)
                return node
            else:
                node.rightChild = traverse(node.rightChild, value)
                return node
        self.root = traverse(self.root, value)

    def minimumDifference(self):
        pass


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


if __name__ == "__main__":
    bt = BinaryTree()
    bt.addNode(2)
    bt.addNode(1)
    bt.addNode(3)
    print(bt.minimumDifference())
