class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        curr = 0

        for r in range(0, len(nums)):
            if nums[r] == 1:
                curr += 1
            else:
                curr = 0
            ans = max(ans, curr)

        return ans

