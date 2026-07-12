class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        # n * (n+log n)
        for i in range(0, len(nums)-k+1):
            # n
            win = [-x for x in nums[i:i+k]]
            # log n
            heapify(win)
            ans.append(-win[0])
        return ans
