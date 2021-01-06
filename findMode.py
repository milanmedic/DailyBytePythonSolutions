# Given a binary search tree, return its mode (you may assume the answer is unique). If the tree is empty, return -1. Note: the mode is the most frequently occurring value in the tree.

# Ex: Given the following tree...

#         2
#        / \
#       1   2
# return 2.


# Ex: Given the following tree...

#          7
#         / \
#       4     9
#      / \   / \
#     1   4 8   9
#                \
#                 9
# return 9.

class BinaryTree:
    def __init__(self):
        self.root = None
        self.entries = dict()

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

    def findMode(self):
        mode = None
        value = 0
        self.populateEntries()
        for entry in self.entries:
            if self.entries[entry] > value:
                mode = entry
                value = self.entries[entry]
        return mode

    def populateEntries(self):
        def traverse(node):
            if node:
                if not self.entries.get(node.value):
                    self.entries[node.value] = 1
                else:
                    self.entries[node.value] = self.entries.get(node.value) + 1
                traverse(node.leftChild)
                traverse(node.rightChild)
        traverse(self.root)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


if __name__ == "__main__":
    bt = BinaryTree()
    bt.addNode(7)
    bt.addNode(4)
    bt.addNode(9)
    bt.addNode(4)
    bt.addNode(1)
    bt.addNode(8)
    bt.addNode(9)
    bt.addNode(9)
    print(bt.findMode())
