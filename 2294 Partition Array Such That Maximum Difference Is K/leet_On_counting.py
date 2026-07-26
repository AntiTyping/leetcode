class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # O(n)
        seen = [False] * (max(nums) + 1)
        # O(n)
        for num in nums:
            seen[num] = True

        ans, anchor = 0, -float('inf')
        for v, present in enumerate(seen):
            if present and v - anchor > k:
                anchor = v
                ans += 1
        return ans