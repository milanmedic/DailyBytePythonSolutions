class Solution:
    def __init__(self, inputString):
        self.input = inputString
        self.uniqueCharacter = ""
        self.charactersInInput = dict()
        self.createInputCharacterDictionary(inputString)

    def createInputCharacterDictionary(self, inputString):
        for character in inputString:
            self.charactersInInput[character] = (
                self.charactersInInput.get(character, 0) + 1
            )

    def findUniqueCharacter(self):
        for character in self.charactersInInput:
            if self.charactersInInput.get(character) == 1:
                self.uniqueCharacter = character
                break

    def getUniqueCharacterIndex(self):
        for index in range(0, len(self.input)):
            if self.input[index] == self.uniqueCharacter:
                return index
        return -1


if __name__ == "__main__":
    solution = Solution("developer")
    solution.findUniqueCharacter()
    print(solution.getUniqueCharacterIndex())
