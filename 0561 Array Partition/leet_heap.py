class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n)
        heapq.heapify(nums)
        ans = 0
        # O(n log n)
        for i in range(0, len(nums), 2):
            # O(log(n))
            ans += min(heapq.heappop(nums), heapq.heappop(nums))

        return ans
