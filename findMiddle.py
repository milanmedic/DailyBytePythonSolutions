# This question is asked by Amazon. Given a non-empty linked list, return the middle node of the list.
# If the linked list contains an even number of elements, return the node closer to the end.

# 1->2->3->null, return 2
# 1->2->3->4->null, return 3
# 1->null, return 1

class Solution:
    def __init__(self, list):
        self.list = list

    def getMiddleElement(self):
        return self.list.findMiddleNode()


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def addNode(self, value):
        if not self.head:
            self.head = ListNode(value)
            self.count += 1
            return self.head

        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next

        currentNode.next = ListNode(value)
        self.count += 1
        return currentNode

    def findMiddleNode(self):
        if not self.head:
            return None

        if self.count % 2 == 0:
            middle = self.count / 2
        else:
            middle = round(self.count/2)

        currentNode = self.head
        while middle > 0:
            currentNode = currentNode.next
            middle -= 1

        return currentNode


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == "__main__":
    list = LinkedList()
    list.addNode(1)
    solution = Solution(list)
    result = solution.getMiddleElement()
