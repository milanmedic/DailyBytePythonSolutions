class Solution:
    def __init__(self, inputList, nthIndex):
        self.inputList = inputList
        self.inputList.removeNthToLastNode(nthIndex)


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

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

    def removeNthToLastNode(self, nthIndex):
        if nthIndex > self.count:
            return

        indexOfNodeToBeRemoved = self.count - nthIndex
        if indexOfNodeToBeRemoved == 0:
            self.head = self.head.next
            self.count -= 1
            return

        currentNode = self.head
        previousNode = self.head

        while indexOfNodeToBeRemoved > 0:
            previousNode = currentNode
            currentNode = currentNode.next
            indexOfNodeToBeRemoved -= 1

        if currentNode.next:
            previousNode.next = currentNode.next
        else:
            previousNode.next = None

        self.count -= 1


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
    solution = Solution(list, 5)
    b = ''
