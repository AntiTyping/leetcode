class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v = [0] * len(nums)

        if len(nums) > 0:
            v[0] = nums[0]
        if len(nums) > 1:
            v[1] = max(nums[:2])

        for i in range(2, len(nums)):
            v[i] = max(v[i - 1], v[i - 2] + nums[i])

        return v[-1]