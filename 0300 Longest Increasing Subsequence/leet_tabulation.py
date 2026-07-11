class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # max
        # state: lengiest subsequence ending at i
        # rec:
        #
        dp = [0] * len(nums)

        for i in range(len(nums)):
            ans = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    ans = max(ans, dp[j] + 1)
            dp[i] = ans

        return max([dp[i] for i in range(len(nums))])
