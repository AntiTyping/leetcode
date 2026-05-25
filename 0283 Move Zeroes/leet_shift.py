class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        l, r = 0, len(nums) - 1
        # n
        while l <= r:
            if nums[l] == 0:
                for i in range(l, r):
                    nums[i] = nums[i + 1]
                nums[r] = 0
                r -= 1
            else:
                l += 1
        return nums