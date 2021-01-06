class Solution:
    def __init__(self):
        self.list = LinkedList()

    def mergeLinkedLists(self, firstList, secondList):
        while firstList.getCurrentNodeValue() or secondList.getCurrentNodeValue():
            firstNodeValue = firstList.getCurrentNodeValue()
            secondNodeValue = secondList.getCurrentNodeValue()

            if not firstNodeValue and not secondNodeValue:
                return self.list

            if firstNodeValue and not secondNodeValue:
                self.list.addNode(firstNodeValue)
                firstList.next()

            if secondNodeValue and not firstNodeValue:
                self.list.addNode(secondNodeValue)
                secondList.next()

            if (firstNodeValue and secondNodeValue) and firstNodeValue <= secondNodeValue:
                self.list.addNode(firstNodeValue)
                firstList.next()
            else:
                self.list.addNode(secondNodeValue)
                secondList.next()
        return self.list


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def addNode(self, value):
        if not self.head:
            self.head = ListNode(value)
            return self.head

        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next

        currentNode.next = ListNode(value)
        return currentNode

    def getCurrentNodeValue(self):
        if not self.head:
            return None
        return self.head.value

    def next(self):
        if self.head:
            self.head = self.head.next


class ListNode:
    def __init__(self, value):
        self.next = None
        self.value = value


if __name__ == "__main__":
    solution = Solution()
    list1 = LinkedList()
    list1.addNode(4)
    list1.addNode(4)
    list1.addNode(7)
    list2 = LinkedList()
    list2.addNode(1)
    list2.addNode(5)
    list2.addNode(6)
    solution.mergeLinkedLists(list1, list2)
