class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        for i in range(k-1, len(nums)):
            if i > k-1:
                if nums[i] > lg:
                    win = [-x for x in nums[i-k+1:i+1]]
                    heapify(win)
                elif nums[i-k] == lg:
                    win = [-x for x in nums[i-k+1:i+1]]
                    heapify(win)
            else:
                win = [-x for x in nums[i-k+1:i+1]]
                heapify(win)
            lg = -win[0]
            ans.append(lg)
        return ans
