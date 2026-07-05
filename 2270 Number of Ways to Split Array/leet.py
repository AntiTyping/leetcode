class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        psum = [0] * len(nums)
        psum[0] = nums[0]
        for i in range(1, len(nums)):
            psum[i] = psum[i - 1] + nums[i]

        ans = 0
        for i in range(0, len(nums) - 1):
            sum_a = psum[i]
            sum_b = psum[len(nums) - 1] - sum_a
            if sum_a >= sum_b:
                ans += 1

        return ans