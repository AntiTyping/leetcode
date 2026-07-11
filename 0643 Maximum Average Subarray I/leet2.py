class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ans = 0
        for i in range(k):
            ans += nums[i]

        curr = ans
        for i in range(k, len(nums)):
            curr += nums[i]
            curr -= nums[i - k]
            ans = max(ans, curr)

        return float(ans) / k
