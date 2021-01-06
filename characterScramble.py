# Given two strings, passage and text return whether or not the characters in text can be used to form the given passage.
# Note: Each character in text may only be used once and passage and text will only contain lowercase alphabetical characters.

# Ex: Given the following passage and text…

# passage = "bat", text = "cat", return false.

# Ex: Given the following passage and text…

# passage = "dog" text = "didnotgo", return true.

class Solution:
    def __init__(self, passage, text):
        self.availableCharacters = self.createCharactersMap(text)
        self.passage = passage

    def createCharactersMap(self, text):
        characterMap = dict()
        for character in text:
            if not characterMap.get(character):
                characterMap[character] = 1
            else:
                characterMap[character] = characterMap[character] + 1
        return characterMap

    def checkForPassageFormation(self):
        for character in self.passage:
            if self.availableCharacters.get(character):
                self.availableCharacters[character] = self.availableCharacters[character] - 1
            else:
                return False

        for character in self.passage:
            if self.availableCharacters[character] < 0:
                return False
        return True


if __name__ == "__main__":
    solution = Solution("dog", "didnotgo")
    print(solution.checkForPassageFormation())
    a = ''
