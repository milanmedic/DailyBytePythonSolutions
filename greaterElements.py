# Given two arrays of numbers, where the first array is a subset of the second array, return an array containing all the next greater elements for each element in the first array, in the second array. If there is no greater element for any element, output - 1 for that number.

# Ex: Given the following arrays…

# nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2], return [-1, 3, -1] because no element in nums2 is greater than 4, 3 is the first number in nums2 greater than 1, and no element in nums2 is greater than 2.
# nums1 = [2, 4], nums2 = [1, 2, 3, 4], return [3, -1] because 3 is the first greater element that occurs in nums2 after 2 and no element is greater than 4.

class Solution:
    def __init__(self, nums1, nums2):
        self.nextGreaterNums = self.findGreaterNums(nums1, nums2)

    def findGreaterNums(self, nums1, nums2):
        nextGreater = []
        for index in range(0, len(nums1)):
            if nums1[index] < nums2[index]:
                nextGreater.append(nums2[index])
            else:
                nextGreaterNumber = self.findNextGreaterNum(
                    index, nums1[index], nums2)
                if nextGreaterNumber != -1:
                    nextGreater.append(nextGreaterNumber)
                else:
                    nextGreater.append(-1)

        return nextGreater

    def findNextGreaterNum(self, startIndex, number, arrayOfNumbers):
        for index in range(startIndex, len(arrayOfNumbers)):
            if number < arrayOfNumbers[index]:
                return arrayOfNumbers[index]
        return -1


if __name__ == "__main__":
    solution = Solution([2, 4], [1, 2, 3, 4])
    b = ''
