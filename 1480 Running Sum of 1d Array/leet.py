class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        psum = [0] * len(nums)
        psum[0] = nums[0]
        for i in range(1, len(nums)):
            psum[i] = psum[i - 1] + nums[i]
        return psum
