class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n)
        n = [0]*(len(nums)+1)

        # O(n)
        for i in nums:
            n[i] = 1

        # O(n)
        for i in range(len(n)):
            if n[i] == 0:
                return i
        # O(n) 1M
        # O(n log n) 20M
