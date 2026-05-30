class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = []

        def backtrack(nums, used):
            # base case
            if len(used) == len(nums):
                o = []
                for i in used:
                    o.append(nums[i])
                out.append(o)
            # go deeper
            for i in range(len(nums)):
                if i in used:
                    continue
                backtrack(nums, used + [i])

        backtrack(nums, [])
        return out
