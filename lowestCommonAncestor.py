# Given a binary search tree that contains unique values and two nodes within the tree, a, and b, return their lowest common ancestor. Note: the lowest common ancestor of two nodes is the deepest node within the tree such that both nodes are descendants of it.

# Ex: Given the following tree...
#        7
#       / \
#     2    9
#    / \
#   1   5
# and a = 1, b = 9, return a reference to the node containing 7.
# Ex: Given the following tree...

#         8
#        / \
#       3   9
#      / \
#     2   6
# and a = 2, b = 6, return a reference to the node containing 3.
# Ex: Given the following tree...

#         8
#        / \
#       6   9
# and a = 6, b = 8, return a reference to the node containing 8.

# Create One array for each number, store path in that array. Find the value that is the same in both arrays

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

    def findLowestCommonAncestor(self, firstNodeValue, secondNodeValue):
        def findPath(value, path):
            def traverse(node, value):
                if node.value == value:
                    return
                if node.value > value:
                    node.leftChild = traverse(node.leftChild, value)
                    path.add(node.value)
                    return node
                else:
                    node.rightChild = traverse(node.rightChild, value)
                    path.add(node.value)
                    return node
            traverse(self.root, value)
            return path

        firstNodePath = findPath(firstNodeValue, set())
        secondNodePath = findPath(secondNodeValue, set())

        crossPaths = firstNodePath.intersection(secondNodePath)
        if not crossPaths:
            if not firstNodePath:
                crossPaths = secondNodePath
            else:
                crossPaths = secondNodePath

        def findMin(inputSet):
            min = float("inf")
            for element in inputSet:
                if element < min:
                    min = element
            return min

        return findMin(crossPaths)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


if __name__ == "__main__":
    bt = BinaryTree()
    bt.insertNode(6)
    bt.insertNode(8)
    bt.insertNode(9)
    print(bt.findLowestCommonAncestor(6, 8))
