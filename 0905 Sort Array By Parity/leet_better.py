class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # partition, two pointers
        l, r = 0, len(nums) - 1
        # O(n)
        while l < r:
            if nums[l] % 2 == 1 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            if nums[l] % 2 == 0:
                l += 1
            if nums[r] % 2 == 1:
                r -= 1
        return nums


