class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        s = 0
        for i in range(k):
            s += nums[i]

        max_sum = s

        for i in range(k, len(nums)):
            s = s + nums[i] - nums[i - k]
            max_sum = max(max_sum, s)

        return float(max_sum) / k
