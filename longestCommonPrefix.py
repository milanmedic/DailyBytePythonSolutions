class Solution:
    def __init__(self, input):
        self.firstArray = input[0]
        self.secondArray = input[1]
        self.thirdArray = input[2]
        self.longestCommonPrefix = ""
        self.smallestLength = 0

    def findSmallestLength(self):
        if len(self.firstArray) < len(self.secondArray):
            self.smallestLength = len(self.firstArray)
        else:
            self.smallestLength = len(self.secondArray)

        if self.smallestLength > len(self.thirdArray):
            self.smallestLength = len(self.thirdArray)
        return

    def findLongestCommonPrefix(self):
        self.findSmallestLength()
        for index in range(0, self.smallestLength):
            if (self.firstArray[index] == self.secondArray[index]) and (
                self.secondArray[index] == self.thirdArray[index]
            ):
                self.longestCommonPrefix += self.firstArray[index]

    def getLongestCommonPrefix(self):
        return self.longestCommonPrefix


if __name__ == "__main__":
    solution = Solution(["spot", "spotty", "spotted"])
    solution.findLongestCommonPrefix()
    print(solution.getLongestCommonPrefix())
