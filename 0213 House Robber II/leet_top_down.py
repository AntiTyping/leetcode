class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        @cache
        def dp(houses, i):
            if i == 0:
                return houses[0]
            if i == 1:
                return max(houses[0], houses[1])

            rob = houses[i] + dp(houses, i - 2)
            skip = dp(houses, i - 1)

            return max(rob, skip)

        first = tuple(nums[:(len(nums) - 1)])
        last = tuple(nums[1:len(nums)])

        f = dp(first, len(first) - 1)
        l = dp(last, len(last) - 1)

        return max(f, l)
