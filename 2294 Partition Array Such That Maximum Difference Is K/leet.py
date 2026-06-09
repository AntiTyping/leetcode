class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = 1
        first = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > first + k:
                first = nums[i]
                n += 1
        return n

