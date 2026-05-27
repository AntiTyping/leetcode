class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # partition, two pointers
        l, r = 0, 0
        # O(n)
        while r < len(nums):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            else:
                r += 1
        return nums


