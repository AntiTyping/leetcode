class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def r(nums):
            @cache
            def dp1(i):
                if i == 0:
                    return nums[0]
                if i == 1:
                    return max(nums[:2])
                return max(dp1(i - 1), dp1(i - 2) + nums[i])
            return dp1(len(nums) - 1)

        ans = max([r(nums[1:]), r(nums[:-1])])

        return ans
