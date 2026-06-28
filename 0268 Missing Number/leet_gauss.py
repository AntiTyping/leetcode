class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        gauss = n * (n + 1) // 2
        for i in nums:
            gauss -= i
        return gauss
