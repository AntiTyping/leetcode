class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        # func: length of the subsequences
        # state: i for 0..i subsequence
        # order: backward
        # recurrence:
        #   find the longiest shorter subsequence where last element is diff smaller
        # base: if len == 1: return 0
        # time: O(n n)
        # space: O(n)

        h = defaultdict(list)
        for i in range(len(arr)):
            a = arr[i]
            h[a].append(i)

        @cache
        def dp(i):
            if i == 0:
                return 1

            ans = 1
            # for j in range(i):
            for j in h[arr[i] - difference]:
                if j < i:
                    ans = max(ans, dp(j) + 1)

            return ans

        return max([dp(l) for l in range(len(arr))])

        # dp = [0] * len(nums)

        # dp[0] = 1

        # for j in range(2, len(arr)):

