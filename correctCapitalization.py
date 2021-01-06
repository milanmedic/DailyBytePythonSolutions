# This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

# Ex: Given the following strings...

# "USA", return true
# "Calvin", return true
# "compUter", return false
# "coding", return true

class Solution:
    def __init__(self, inputString):
        self.input = inputString

    def checkCapitalization(self):
        for index, character in enumerate(self.input, start=0):
            if index != 0 and (ord(character) >= 65 and ord(character) <= 90):
                if not (ord(self.input[0]) >= 65 and ord(self.input[0]) <= 90):
                    return False

        return True


if __name__ == "__main__":
    solution = Solution("compUter")
    print(solution.checkCapitalization())
    solution2 = Solution("USA")
    print(solution2.checkCapitalization())
