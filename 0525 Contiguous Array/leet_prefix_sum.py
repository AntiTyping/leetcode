class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = [0] * len(nums)
        p[0] = nums[0]
        for i in range(1, len(nums)):
            p[i] = p[i - 1] + nums[i]

        ans = 0
        for l in range(len(nums)):  # 0, 1, 2 ; 3
            for r in range(l + 1, len(nums)):  # 1,2 ; 3
                if (r - l + 1) % 2 == 0 and p[r] - p[l] + nums[l] == (r - l + 1) // 2:
                    ans = max(ans, r - l + 1)
        return ans