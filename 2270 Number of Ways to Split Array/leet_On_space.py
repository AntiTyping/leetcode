class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tsum = sum(nums)
        psum = 0
        ans = 0
        for i in range(0, len(nums) - 1):
            psum += nums[i]
            ssum = tsum - psum
            if psum >= ssum:
                ans += 1

        return ans