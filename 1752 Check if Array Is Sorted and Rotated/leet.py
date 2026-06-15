class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    return False
        else:
            split = -1
            for j in range(len(nums) - 1, 0, -1):
                if nums[j - 1] > nums[j]:
                    split = j
                    break

            for i in range(1, split):
                if nums[i - 1] > nums[i]:
                    return False

            for i in range(split + 1, len(nums)):
                if nums[i - 1] > nums[i]:
                    return False

        return True
