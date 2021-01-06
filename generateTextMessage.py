# This question is asked by Google. Given a string of digits, return all possible text messages those digits could send. Note: The mapping of digits to letters is as follows…

# 0 -> null
# 1 -> null
# 2 -> "abc"
# 3 -> "def"
# 4 -> "ghi"
# 5 -> "jkl"
# 6 -> "mno"
# 7 -> "pqrs"
# 8 -> "tuv"
# 9 -> "wxyz"

# Ex: digits = "23" return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

# current solution is O(n^3) which is terribly inefficient. Go thorugh an algorithms course
class Solution:
    def __init__(self, digits):
        self.digits = digits
        self.mappings = self.createDigitMapping()
        self.possibleMessages = set()

    def createDigitMapping(self):
        mappings = dict()
        mappings[0] = None
        mappings[1] = None
        mappings[2] = "abc"
        mappings[3] = "def"
        mappings[4] = "ghi"
        mappings[5] = "jkl"
        mappings[6] = "mno"
        mappings[7] = "pqrs"
        mappings[8] = "tuv"
        mappings[9] = "wxyz"
        return mappings

    def getPossibleMessages(self):
        # for each number in first letter, create a combo with each letter in second number
        pass


if __name__ == "__main__":
    solution = Solution("23")
