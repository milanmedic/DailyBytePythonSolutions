# Given an array of numbers sorted in ascending order, return a height balanced binary search tree using every number from the array. Note: height balanced meaning that the level of any node’s two subtrees should not differ by more than one.

# Ex: nums = [1, 2, 3] return a reference to the following tree...
#        2
#       /  \
#      1    3

# Ex: nums = [1, 2, 3, 4, 5, 6] return a reference to the following tree...
#         3
#        / \
#      2    5
#     /   /  \
#   1    4    6

# def convert(begin, end):
#             if begin > end:
#                 return None
#             middle = math.floor((begin+end)/2)
#             node = TreeNode(inputArray[middle])
#             node.leftChild = convert(begin, middle - 1)
#             node.rightChild = convert(middle+1, end)
#             return node
import math


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
        self.root = traverse(self.root, value)

    def convertArrayToBST(self, inputArray):
        def convert(begin, end):
            if begin > end:
                return None
            middle = math.floor((begin+end)/2)
            node = TreeNode(inputArray[middle])
            node.leftChild = convert(begin, middle - 1)
            node.rightChild = convert(middle+1, end)
            return node
        self.root = convert(0, len(inputArray)-1)


class TreeNode:
    def __init__(self, value):
        self.rightChild = None
        self.leftChild = None
        self.value = value


if __name__ == "__main__":
    bt = BinaryTree()
    bt.convertArrayToBST([1, 2, 3, 4, 5, 6])
    a = ''
