class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        closest = float('inf')

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if abs(target - total) < abs(closest - target):
                    closest = total

                if closest == target:
                    return closest

                if total > target:
                    r -= 1
                else:
                    l += 1

        return closest
