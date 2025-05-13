class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) -1

        while True:
            if numbers[i] + numbers[j] == target:
                return (i + 1, j + 1)
            if numbers[i] + numbers[j] > target: # i make mistake here
                j -= 1
            else:
                i += 1

        return (0, 0)