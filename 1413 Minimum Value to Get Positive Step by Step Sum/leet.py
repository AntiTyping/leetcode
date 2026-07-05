class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        psum = [0] * len(nums)
        psum[0] = nums[0]
        minv = nums[0]
        for i in range(1, len(nums)):
            psum[i] = psum[i - 1] + nums[i]
            minv = min(minv, psum[i])

        if minv < 0:
            return 1 - minv

        return 1


