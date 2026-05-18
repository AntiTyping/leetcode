class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        right = 0

        while right < len(nums):
            # 12342
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
                right += 1
            else:
                right += 1
        return left
