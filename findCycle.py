class NodeNotFoundError(Exception):
    def __init__(self, value):
        self.message = 'Node with value: ' + value + ' not found.'


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

    def setCycle(self, startNodeValue, endNodeValue):
        startNode = self.head
        while startNode.next and startNode.value != startNodeValue:
            startNode = startNode.next

        if not startNode:
            raise NodeNotFoundError(startNodeValue)

        endNode = self.head
        while endNode.next and endNode.value != endNodeValue:
            endNode = endNode.next

        if not endNode:
            raise NodeNotFoundError(endNodeValue)

        startNode.setNext(endNode)

        return

    def findCycle(self):
        encounteredNodes = set()

        currentNode = self.head
        while currentNode.next:
            if not currentNode in encounteredNodes:
                encounteredNodes.add(currentNode)
                currentNode = currentNode.next
            else:
                return currentNode
        return None


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def setNext(self, nextNode):
        self.next = nextNode


if __name__ == "__main__":
    list = LinkedList()
    list.addNode(1)
    list.setCycle(1, 1)
    list.findCycle()
    b = ''
