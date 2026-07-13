class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        ans = 0
        curr = []
        l = 0
        for r in range(len(nums)):
            diff = abs(max(nums[l:r + 1]) - min(nums[l:r + 1]))  # 0
            while l <= r and diff > limit:
                l += 1
                diff = abs(max(nums[l:r + 1]) - min(nums[l:r + 1]))
            ans = max(ans, r - l + 1)
        return ans


