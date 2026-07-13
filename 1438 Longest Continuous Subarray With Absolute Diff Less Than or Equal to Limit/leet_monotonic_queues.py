class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        ans = 0
        minq = deque()
        maxq = deque()

        l = 0
        for r in range(len(nums)):
            num = nums[r]

            while minq and minq[-1] > num:
                minq.pop()

            while maxq and maxq[-1] < num:
                maxq.pop()

            minq.append(num)
            maxq.append(num)

            while maxq[0] - minq[0] > limit:
                if nums[l] == maxq[0]:
                    maxq.popleft()
                if nums[l] == minq[0]:
                    minq.popleft()
                l += 1
            ans = max(ans, r - l + 1)
        return ans


