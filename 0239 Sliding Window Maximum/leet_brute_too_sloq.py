class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        # n2
        for i in range(len(nums) - k + 1):
            ans.append(max(nums[i:k + i]))
        return ans
