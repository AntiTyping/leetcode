class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        n = 0
        l, r = 0, 0

        while r < len(nums):
            if nums[r] - nums[l] == 1:
                if r - l + 1 > n:
                    n = r - l + 1
                r += 1
            elif nums[r] - nums[l] > 1:
                l += 1
            else:
                r += 1

        return n
