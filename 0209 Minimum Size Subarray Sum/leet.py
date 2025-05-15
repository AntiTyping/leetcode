class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        p = [0] * len(nums)
        p[0] = nums[0]
        for i in range(1, len(nums)):
            p[i] = p[i - 1] + nums[i]

        min_l = len(nums) + 1
        i, j = 0, 0

        while i < len(nums) and j < len(nums):
            if i == 0:
                if p[j] >= target:
                    min_l = min(min_l, j - i + 1)
                    i += 1
                else:
                    j += 1
            else:
                if p[j] - p[i - 1] >= target:
                    min_l = min(min_l, j - i + 1)
                    i += 1
                else:
                    j += 1

        if min_l == len(nums) + 1:
            return 0
        else:
            return min_l


print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))