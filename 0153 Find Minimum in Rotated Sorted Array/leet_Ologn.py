class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        min_n = nums[0]
        while l <= r:
            m = l + (r - l) // 2
            # left sorted
            # 45|6|7123
            if nums[l] <= nums[m]:
                min_n = min(min_n, nums[l])
                l = m + 1 # check the other side
            # 671|2|34
            if nums[m] <= nums[r]:
                min_n = min(min_n, nums[m])
                r = m - 1 # check the other side
        return min_n

