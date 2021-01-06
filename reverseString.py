class Solution:
    def __init__(self, inputString):
        self.result = self.reverseString(list(inputString))

    def reverseString(self, inputString):
        if len(inputString) == 0 or len(inputString) == 1:
            return inputString

        for index in range(0, round(len(inputString)/2)):
            temp = inputString[index]
            inputString[index] = inputString[len(inputString)-index-1]
            inputString[len(inputString)-index-1] = temp
        return ''.join(inputString)

    def getResult(self):
        return self.result


if __name__ == "__main__":
    solution = Solution("helloworl")
    b = ''
