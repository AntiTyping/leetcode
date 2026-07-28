class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def div(m):
            chunks = 1
            curr = 0
            for num in nums:
                if curr + num > m:
                    chunks += 1
                    curr = num
                else:
                    curr += num
            return chunks

        l, r = max(nums), sum(nums)
        while l <= r:
            m = (l + r) // 2
            if div(m) <= k:
                r = m - 1
            else:
                l = m + 1

        return l