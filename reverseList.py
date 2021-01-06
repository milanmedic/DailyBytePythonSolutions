# Given a linked list, containing unique values, reverse it, and return the result.

# Ex: Given the following linked lists...

# 1->2->3->null, return a reference to the node that contains 3 which points to a list that looks like the following: 3->2->1->null
# 7->15->9->2->null, return a reference to the node that contains 2 which points to a list that looks like the following: 2->9->15->7->null
# 1->null, return a reference to the node that contains 1 which points to a list that looks like the following: 1->null

class LinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def addNode(self, value):
        self.count += 1
        if not self.head:
            self.head = ListNode(value)
            return self.head

        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = ListNode(value)
        return currentNode

    def reverseList(self):
        currentNode = self.head
        previousNode = None
        tempNode = None

        while currentNode:
            tempNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = tempNode

        self.head = previousNode

    # def reverseList(self):
    #     interimList = []
    #     currentNode = self.head
    #     while currentNode:
    #         interimList.append(currentNode.value)
    #         currentNode = currentNode.next

    #     self.head = None
    #     self.count = 0
    #     interimList.reverse()
    #     for nodeValue in interimList:
    #         self.addNode(nodeValue)
    #     return


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == "__main__":
    list = LinkedList()
    list.addNode(1)
    list.addNode(2)
    list.addNode(3)
    list.addNode(4)
    list.addNode(5)
    list.reverseList()
    b = ''
