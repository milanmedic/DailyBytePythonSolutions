class Solution:
    def __init__(self, firstInput, secondInput):
        self.firstString = firstInput
        self.secondString = secondInput
        self.charactersInFirstString = dict()
        self.populateCharacterDictionary()

    def populateCharacterDictionary(self):
        for character in self.firstString:
            if not (character in self.charactersInFirstString):
                self.charactersInFirstString[character] = (
                    self.charactersInFirstString.get(character, 0) + 1
                )

    def checkForAnagram(self):
        for character in self.secondString:
            if not (character in self.charactersInFirstString):
                return False
            else:
                self.charactersInFirstString[character] = (
                    self.charactersInFirstString.get(character) - 1
                )
        return self.checkForNonZerosInDict()

    def checkForNonZerosInDict(self):
        for value in self.charactersInFirstString.values():
            if value != 0:
                return False
            return True


if __name__ == "__main__":
    solution = Solution("program", "function")
    print(solution.checkForAnagram())
