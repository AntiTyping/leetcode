class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        curr = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                curr += 1
            while curr > k:
                if nums[l] == 0:
                    curr -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans