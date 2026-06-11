class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vv = [0] * len(nums)
        memo = {}

        def dp(n):
            if n == 0:
                vv[0] = nums[0]
                return nums[0]
            elif n == 1:
                vv[1] = max(nums[:2])
                return max(nums[:2])
            else:
                if n - 1 in memo:
                    v1 = memo[n - 1]
                else:
                    v1 = dp(n - 1)
                    memo[n - 1] = v1
                if n - 2 in memo:
                    v2 = memo[n - 2]
                else:
                    v2 = dp(n - 2)
                    memo[n - 2] = v1
                if v1 > v2 + nums[n]:
                    vv[n] = v1
                    return v1
                else:
                    vv[n] = v2 + nums[n]
                    return v2 + nums[n]

        v = dp(len(nums) - 1)

        return v