class Stack:
    def __init__(self):
        self.head = None
        self.top = None

    def push(self, value):
        if not self.head:
            self.head = StackItem(value)
            self.top = self.head
            return self.head

        currentItem = self.head
        while currentItem.next:
            currentItem = currentItem.next

        currentItem.next = StackItem(value)
        self.top = currentItem.next
        return self.top

    def pop(self):
        current = self.head
        while current.next.next:
            current = current.next

        returnValue = current.next
        current.next = None
        self.top = current
        return returnValue

    def peek(self):
        return self.top

    def isEmpty(self):
        if not self.head:
            return True
        return False


class StackItem:
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.peek()
    stack.isEmpty()
    stack.pop()
    stack.pop()
    stack.peek()
