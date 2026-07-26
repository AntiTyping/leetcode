class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l = 0
        r = 0
        ans = 1
        while r < len(nums):
            diff = nums[r] - nums[l]
            if diff <= k:
                r += 1
            else:
                ans += 1
                l = r
        return ans