class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        counts[0] = -1

        m = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += -1
            else:
                count += 1

            if count in counts:
                if i - counts[count] > m:
                    m = i - counts[count]
            else:
                counts[count] = i

        return m
