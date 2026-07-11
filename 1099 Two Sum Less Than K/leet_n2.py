class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = {}
        max_ = -1

        # O(n)
        for i in range(1, len(nums)):
            # O(n)
            for j in range(0, i):
                s = nums[i] + nums[j]
                if s > max_ and s < k:
                    max_ = s

        return max_