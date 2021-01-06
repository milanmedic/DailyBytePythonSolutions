# This question is asked by Amazon. Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.

# Ex: Given the following strings...

# "LR", return true
# "URURD", return false
# "RUULLDRD", return true

class Solution:
    def __init__(self, inputString):
        self.input = inputString
        self.directions = dict()
        self.directions["L"] = 0
        self.directions["R"] = 0
        self.directions["U"] = 0
        self.directions["D"] = 0

    def addDirections(self):
        for direction in self.input:
            self.directions[direction] = self.directions[direction]+1

    def checkPathValidity(self):
        if self.directions['L'] == self.directions['R'] and self.directions['U'] == self.directions['D']:
            return True
        return False

    # def checkDirections(self):
    #     for direction in self.input:
    #         if direction == 'L':
    #             self.directions['R'] = self.directions.get('R') - 1
    #         elif direction == 'U':
    #             self.directions['D'] = self.directions.get('D') - 1
    #         elif direction == 'R':
    #             self.directions['L'] = self.directions.get('L') - 1
    #         elif direction == 'D':
    #             self.directions['U'] = self.directions.get('U') - 1

    # def checkPathValidity(self):
    #     for direction in self.directions:
    #         if self.directions[direction] != 0:
    #             return False
    #     return True


if __name__ == "__main__":
    solution = Solution("LURD")
    solution.addDirections()
    # solution.checkDirections()
    print(solution.checkPathValidity())
