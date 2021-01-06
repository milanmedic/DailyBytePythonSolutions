# Create a class CallCounter that tracks the number of calls a client has made within the last 3 seconds. Your class should contain one method, ping(int t) that receives the current timestamp (in milliseconds) of a new call being made and returns the number of calls made within the last 3 seconds.
# Note: you may assume that the time associated with each subsequent call to ping is strictly increasing.

# Ex: Given the following calls to ping…

# ping(1), return 1 (1 call within the last 3 seconds)
# ping(300), return 2 (2 calls within the last 3 seconds)
# ping(3000), return 3 (3 calls within the last 3 seconds)
# ping(3002), return 3 (3 calls within the last 3 seconds)
# ping(7000), return 1 (1 call within the last 3 seconds)


# Call the class
# 	1. Remember the timestamp of the first call
#   2. If subsequent call timestamp - first call timestamp < 3 seconds -> increase the counter

import time


def GetCurrentTimestamp():
    return int(round(time.time() * 1000))


class CallCounter:
    def __init__(self):
        self.firstCallTimestamp = GetCurrentTimestamp()  # first timestamp
        self.numberOfCalls = 1

    def ping(self, newTimestamp):
        if newTimestamp - self.firstCallTimestamp < 3:
            self.numberOfCalls += 1
        return self.numberOfCalls


if __name__ == "__main__":
    callCounter = CallCounter()
