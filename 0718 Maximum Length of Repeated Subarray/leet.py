class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * len(nums2) for _ in range(len(nums1))]

        for r in range(len(nums1)):
            for c in range(len(nums2)):
                if nums1[r] == nums2[c]:
                    if r < 1 or c < 1:
                        a = 0
                    else:
                        a = dp[r - 1][c - 1]
                    dp[r][c] = a + 1
        return max(max(r) for r in dp)


print(Solution().findLength([0,0,0,0,1], [1,0,0,0,0]))