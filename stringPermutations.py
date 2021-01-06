# Case 1: Return original string
# Case 2: Return multiple variations of the same input string where
# only one character was uppercased/lowercased at a time
# Case 3: recursively return variations of the same input string where
# each consecutive character is being uppercassed / lowercased
# Case 4: Same as three just backwards
#
#

class Solution:
    def __init__(self, inputString):
        self.inputString = inputString
        self.permutations = set()

    def getAllPermutations(self):
        self.permutations.add(self.inputString)  # case 1

        for index in range(0, len(self.inputString)):
            if self.checkIfCharacter(self.inputString[index]):
                self.permutations.add(
                    self.getSingleCharacterChangeVariation(index))  # case 2

        iterativePermutations = self.getAllIterativePermutations()
        for permutation in iterativePermutations:
            self.permutations.add(permutation)

        return self.permutations

    def getAllIterativePermutations(self):
        permutations = []
        permutation = self.permutate(0, self.inputString, permutations, 1)
        permutation = self.permutate(
            len(permutation) - 1, permutation, permutations, -1)
        return permutations

    def permutate(self, index, permutation, permutations, direction):
        if index == len(self.inputString) or index == -1:
            return permutation
        else:
            if self.checkIfCharacter(permutation[index]):
                if self.checkIfLowercase(permutation[index]):
                    permutation = self.upperCaseLetterInInput(
                        index, permutation)
                    permutations.append(permutation)
                else:
                    permutation = self.lowerCaseLetterInInput(
                        index, permutation)
                    permutations.append(permutation)
        if direction == 1:
            return self.permutate(index+1, permutation, permutations, 1)
        else:
            return self.permutate(index-1, permutation, permutations, -1)

    def checkIfCharacter(self, arrayMember):
        charCode = ord(arrayMember)
        if (charCode >= 65 and charCode <= 90) or (charCode >= 97 and charCode <= 122):
            return True
        return False

    def getSingleCharacterChangeVariation(self, index):
        newVariation = None

        if self.checkIfLowercase(self.inputString[index]):
            newVariation = self.upperCaseLetterInInput(index, self.inputString)
        else:
            newVariation = self.lowerCaseLetterInInput(index, self.inputString)

        return newVariation

    def checkIfLowercase(self, character):
        charCode = ord(character)
        if charCode >= 97 and charCode <= 122:
            return True
        return False

    def upperCaseLetterInInput(self, index, inputString):
        letter = inputString[index].upper()
        retVal = ''
        retVal = inputString[0:index] + letter + \
            inputString[index + 1:len(inputString)]
        return retVal

    def lowerCaseLetterInInput(self, index, inputString):
        letter = inputString[index].lower()
        retVal = ''
        retVal = inputString[0:index] + letter + \
            inputString[index + 1:len(inputString)]
        return retVal


if __name__ == "__main__":
    solution = Solution("c7w2M")
    print(solution.getAllPermutations())
    a = ''
