# Given a binary search tree, rearrange the tree such that it forms a linked list where all its values are in ascending order.

# Ex: Given the following tree...
#         5
#        / \
#       1   6

# return...

# 1
#  \
#   5
#    \
#     6

# Ex: Given the following tree...

#        5
#       / \
#     2    9
#    / \
#   1   3

# return...

# 1
#  \
#   2
#    \
#     3
#      \
#       5
#        \
#         9

# Ex: Given the following tree...

# 5
#  \
#   6

# return...

# 5
#  \
#   6

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

    # def convertToLinkedList(self):
    #     list = LinkedList()

    #     def traverse(node):
    #         if node.leftChild:
    #             traverse(node.leftChild)
    #         if node:
    #             list.insertNode(node.value)
    #         if node.rightChild:
    #             traverse(node.rightChild)

    #     traverse(self.root)
    #     return list

    def convertToLinkedList(self):
        list = LinkedList()

        def traverse(node, list):
            if node.leftChild:
                list = traverse(node.leftChild, list)
            if node:
                list.insertNode(node.value)
                if node.rightChild:
                    list = traverse(node.rightChild, list)
                return list

        list = traverse(self.root, list)
        return list


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, value):
        if not self.head:
            self.head = ListNode(value)
            return self.head

        currentNode = self.head

        while currentNode.next:
            currentNode = currentNode.next

        currentNode.next = ListNode(value)
        return currentNode


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == "__main__":
    bt = BinaryTree()
    bt.insertNode(2)
    bt.insertNode(1)
    bt.insertNode(3)
    bt.insertNode(4)
    bt.insertNode(3.5)
    bt.insertNode(5)
    list = bt.convertToLinkedList()
    a = ''
