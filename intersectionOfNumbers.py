class Solution:
    def __init__(self, firstArray, secondArray):
        self.firstNums = firstArray
        self.secondNums = secondArray
        self.uniqueNums = set()
        self.populateUniqueNums()

    def populateUniqueNums(self):
        for num in self.firstNums:
            self.uniqueNums.add(num)

    def findIntersection(self):
        intersection = []
        for num in self.secondNums:
            if num in self.uniqueNums:
                intersection.append(num)
        return intersection


if __name__ == "__main__":
    solution = Solution([2, 4, 4, 2], [2, 4])
    print(solution.findIntersection())
