class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # [1,12,-5,-6,50,3], k = 4
        #  0  1. 2. 3. 4

        p = [0] * len(nums)
        p[0] = nums[0]
        for i in range(1, len(nums)):
            p[i] = p[i - 1] + nums[i]

        print(p)
        m = float('-inf')

        for i in range(k - 1, len(nums)):
            if i == k - 1:
                m = max(m, p[i])
            else:
                m = max(m, p[i] - p[i - k])
        return m / float(k)

