class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums)-1
        for i in reversed(range(len(nums))):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False