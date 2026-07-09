class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        # O(n^3)
        for l in range(len(nums)): # 0, 1, 2 ; 3
            for r in range(l+1, len(nums)): # 1,2 ; 3
                if (r - l + 1) % 2 == 0 and sum(nums[l:r+1]) == (r - l + 1) // 2:
                    ans = max(ans, r - l + 1)
        return ans