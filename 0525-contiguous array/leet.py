class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = {0: -1}
        sum = 0

        max_l = 0

        for i in range(len(nums)):
            a = nums[i]
            if a == 0:
                sum += -1
            else:
                sum += 1
            if sum not in sums:
                sums[sum] = i
            else:
                max_l = max(i - sums[sum], max_l)

        return max_l

Solution().findMaxLength([0, 1])