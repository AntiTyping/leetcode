class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = []

        def backtrack(curr, i):
            if i > len(nums):
                return
            out.append(curr[:])
            for k in range(i, len(nums)):
                curr.append(nums[k])
                backtrack(curr, k + 1)
                curr.pop()

        backtrack([], 0)

        return out