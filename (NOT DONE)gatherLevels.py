# Given a binary tree, return its level order traversal where the nodes in each level are ordered from left to right.

# Ex: Given the following tree...

#     4
#    / \
#   2   7
# return [[4], [2, 7]]

# Ex: Given the following tree...

#     2
#    / \
#   10  15
#         \
#          20
# return [[2], [10, 15], [20]]

# Ex: Given the following tree...

#     1
#    / \
#   9   32
#  /      \
# 3        78
# return [[1], [9, 32], [3, 78]]

class BinaryTree:
    def __init__(self):
        self.root = None
        self.levels = list()

    def addNode(self, value):
        def traverse(node):
            if not node:
                node = TreeNode(value)
                return node
            if node.value > value:
                node.leftChild = traverse(node.leftChild)
                return node
            else:
                node.rightChild = traverse(node.rightChild)
                return node
        self.root = traverse(self.root)

    def levelOrder(self):
        def traverse(node):
            if not node:
                return
            if node.leftChild:
                left = traverse(node.leftChild)
            if node.rightChild:
                right = traverse(node.rightChild)
            return node

        traverse(self.root)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


if __name__ == "__main__":
    bt = BinaryTree()
    bt.addNode(9)
    bt.addNode(1)
    bt.addNode(32)
    bt.addNode(3)
    bt.addNode(78)
    bt.levelOrder()
    a = ""
