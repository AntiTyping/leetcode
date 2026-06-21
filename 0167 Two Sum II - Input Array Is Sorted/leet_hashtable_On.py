class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in h:
                return [h[diff]+1, i+1]
            else:
                h[numbers[i]] = i
        return None