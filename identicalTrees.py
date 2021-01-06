# Given two binary trees, return whether or not the two trees are identical. Note: identical meaning they exhibit the same structure and the same values at each node. Ex: Given the following trees...

#         2
#        / \
#       1   3

#     2
#    / \
#   1   3


# return true.

# Ex: Given the following trees...

#         1
#          \
#           9
#            \
#            18

#     1
#    /
#   9
#    \
#     18


# return false.

# Ex: Given the following trees...

#         2
#        / \
#       3   1

#     2
#    / \
#   1   3


# return false.

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

    def addNodeReverse(self, value):

        def traverse(node, value):
            if not node:
                node = TreeNode(value)
                return node
            if node.value < value:
                node.leftChild = traverse(node.leftChild, value)
                return node
            else:
                node.rightChild = traverse(node.rightChild, value)
                return node
        self.root = traverse(self.root, value)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


def compareBinaryTrees(firstTree, secondTree):
    def traverse(firstNode, secondNode):
        if firstNode.value != secondNode.value:
            return False
        if firstNode.leftChild and secondNode.leftChild:
            return traverse(firstNode.leftChild, secondNode.leftChild)
        if firstNode.rightChild and secondNode.rightChild:
            return traverse(firstNode.rightChild, secondNode.rightChild)

    flag = traverse(firstTree.root, secondTree.root)
    if flag == False:
        return False

    return True


if __name__ == "__main__":
    bt1 = BinaryTree()
    bt2 = BinaryTree()
    bt1.addNode(2)
    bt1.addNode(1)
    bt1.addNode(3)
    bt2.addNode(2)
    bt2.addNode(1)
    bt2.addNode(3)
    print(compareBinaryTrees(bt1, bt2))
