# This question is asked by Microsoft. Design a class, MovingAverage, which contains a method, next that is responsible for returning the moving average from a stream of integers.
# Note: a moving average is the average of a subset of data at a given point in time.

# Ex: Given the following series of events...

# // i.e. the moving average has a capacity of 3.
# MovingAverage movingAverage = new MovingAverage(3);
# m.next(3) returns 3 because (3 / 1) = 3
# m.next(5) returns 4 because (3 + 5) / 2 = 4
# m.next(7) = returns 5 because (3 + 5 + 7) / 3 = 5
# m.next(6) = returns 6 because (5 + 7 + 6) / 3 = 6

# MovingAverage class definition:

# public class MovingAverage {
#     // TODO: declare any instance variables you require.
# /**
#  * Initializes a MovingAverage with a
#  * capacity of `size`.
#  */
# public MovingAverage(int size) {
#   // TODO: initialize your MovingAverage.
# }

# /**
#  * Adds `val` to the stream of numbers
#  * and returns the current average of the numbers.
#  */
# public double next(int val) {
#    // TODO: implement this method.
# }
# }

class MovingAverage:
    def __init__(self, maxQueueSize):
        self.maxQueueSize = maxQueueSize
        self.queue = Queue(maxQueueSize)  # queue has a maximum size of 3
        pass

    def addToQueue(self, value):
        self.queue.pushItem(value)

    def removeFromQueue(self):
        self.queue.popItem()

    def next(self, value):
        if self.queue.size == self.maxQueueSize:
            self.removeFromQueue()
        else:
            self.addToQueue(value)
        return self.queue.returnItemsAverage()


class Queue:
    def __init__(self, maxSize):
        self.head = None
        self.size = 0

    def pushItem(self, value):

        self.size += 1
        if not self.head:
            self.head = QueueItem(value)
            return self.head

        currentItem = self.head
        while currentItem.next:
            currentItem = currentItem.next

        currentItem.next = QueueItem(value)
        return currentItem.next

    def popItem(self):
        self.size -= 1
        if self.head.next:
            self.head = self.head.next
            return self.head

        self.head = None
        return self.head

    def returnItemsAverage(self):
        sum = 0
        currentItem = self.head
        while currentItem:
            sum += currentItem.value
            currentItem = currentItem.next

        return round(sum/self.size)


class QueueItem:
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == "__main__":
    movingaverage = MovingAverage(3)
    print(movingaverage.next(3))
    print(movingaverage.next(5))
    print(movingaverage.next(7))
    print(movingaverage.next(6))
    b = ''
