class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return nums
        ans = [-1] * len(nums)

        psum = [0] * len(nums)
        psum[0] = nums[0]
        for i in range(1, len(nums)):
            psum[i] = psum[i - 1] + nums[i]

        for i in range(k, len(nums) - k):
            if i == k:
                ans[i] = (psum[i + k]) / (2 * k + 1)
            else:
                ans[i] = (psum[i + k] - psum[i - k - 1]) / (2 * k + 1)

        return ans
