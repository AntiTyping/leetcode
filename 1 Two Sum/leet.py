class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers = {}

        for i in range(len(nums)):
            d = target - nums[i]
            if d in numbers:
                return (numbers[d], i)
            else:
                numbers[nums[i]] = i

        return (0, 0)
