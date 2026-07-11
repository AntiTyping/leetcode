class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # max
        # state: lengiest subsequence ending at i
        # rec:
        #

        @cache
        def dp(i):
            if i == 0:
                return 1
            else:
                ans = 1
                for j in range(i):
                    if nums[j] < nums[i]:
                        ans = max(dp(j) + 1, ans)
            return ans

        return max([dp(i) for i in range(len(nums))])
