class Solution:
    def __init__(self, inputList, value):
        inputList.removeValue(value)


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

    def removeValue(self, value):

        iterator = 0

        while iterator != self.count:

            while self.head.value == value:
                self.head = self.head.next
                self.count -= 1
                if not self.head:
                    return

            currentNode = self.head
            previousNode = self.head

            if currentNode.value == value:
                if currentNode.next:
                    previousNode.next = currentNode.next
                    self.count -= 1
                    iterator -= 1
                else:
                    previousNode.next = None
                    self.count -= 1
                    iterator -= 1
            previousNode = currentNode
            currentNode = currentNode.next
            iterator += 1

        return


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == "__main__":
    list = LinkedList()
    list.addNode(1)
    list.addNode(1)
    list.addNode(1)
    list.addNode(1)
    list.addNode(1)
    list.addNode(1)
    list.addNode(1)
    solution = Solution(list, 1)
    b = ''
