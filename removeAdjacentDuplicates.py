# This question is asked by Facebook. Given a string s containing only lowercase letters, continuously remove adjacent characters that are the same and return the result.

# Ex: Given the following strings...

# s = "abccba", return ""
# s = "foobar", return "fbar"
# s = "abccbefggfe", return "a"


class Solution:
    def __init__(self, inputString):
        self.input = self.removeAdjacentCharacters(inputString)

    def removeAdjacentCharacters(self, inputString):
        adjacentIndex = self.findAdjacentIndex(inputString)
        if adjacentIndex == -1:
            return inputString
        else:
            inputString = self.removeAdjacent(inputString, adjacentIndex)
            return self.removeAdjacentCharacters(inputString)

    def findAdjacentIndex(self, inputString):
        for index in range(0, len(inputString)-1):
            if inputString[index] == inputString[index+1]:
                return index
        return -1

    def removeAdjacent(self, inputString, index):
        return inputString[0:index] + inputString[index+2:len(inputString)]


if __name__ == "__main__":
    solution = Solution("abccbefggfe")
    b = ''
