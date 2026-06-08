class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n log n)
        nums.sort()
        ans = 0
        # O(n)
        for i in range(0, len(nums), 2):
            ans += nums[i]

        return ans
