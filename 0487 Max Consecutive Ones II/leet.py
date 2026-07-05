class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        curr = 0
        l = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                curr += 1
            while curr > 1:
                if nums[l] == 0:
                    curr -= 1
                l += 1
            ans = max(ans, i - l + 1)

        return ans