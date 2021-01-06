# This question is asked by Google. Given the reference to the root of a binary search tree and a search value, return the reference to the node that contains the value if it exists and null otherwise.
# Note: all values in the binary search tree will be unique.

# Ex: Given the tree...

#         3
#        / \
#       1   4
# and the search value 1 return a reference to the node containing 1.

# Ex: Given the tree

#         7
#        / \
#       5   9
#          / \
#         8   10
# and the search value 9 return a reference to the node containing 9.

# Ex: Given the tree

#         8
#        / \
#       6   9
# and the search value 7 return null.

class BinaryTree:
    def __init__(self):
        self.root = None

    def insertNode(self, value):
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

    def findValue(self, value):
        if self.root == None:
            return -1

        def traverse(node, value):
            if not node:
                return

            if node.value == value:
                return node

            if node.value > value:
                return traverse(node.leftChild, value)
            else:
                return traverse(node.rightChild, value)

        return traverse(self.root, value)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


if __name__ == "__main__":
    bt = BinaryTree()
    bt.insertNode(2)
    bt.insertNode(3)
    bt.insertNode(1)
    bt.insertNode(4)
    print(bt.findValue(4))
    b = ''
