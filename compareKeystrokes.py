# This question is asked by Amazon. Given two strings s and t, which represents a sequence of keystrokes, where # denotes a backspace, return whether or not the sequences produce the same result.

# Ex: Given the following strings...

# s = "ABC#", t = "CD##AB", return true
# s = "como#pur#ter", t = "computer", return true
# s = "cof#dim#ng", t = "code", return false

class Solution:
    def __init__(self, s: list, t: list):
        self.firstString = self.formatInput(s)
        self.secondString = self.formatInput(t)

    def formatInput(self, inputString):
        formattedInput = []
        for character in inputString:
            if character == '#':
                formattedInput.pop()
            else:
                formattedInput.append(character)

        return formattedInput

    def checkInputEquality(self) -> bool:
        if self.secondString == self.firstString:
            return True
        return False


if __name__ == "__main__":
    solution = Solution('cof#dim#ng', 'code')
    print(solution.checkInputEquality())
