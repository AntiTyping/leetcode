class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = []
        # , O(n)
        used = [False] * len(nums)

        def backtrack(curr):
            if len(curr) == len(nums):
                out.append(curr[:])
                return
            # O(n)
            for n in range(len(nums)):
                # O(n)
                if not used[n]:
                    used[n] = True
                    curr.append(nums[n])
                    backtrack(curr)
                    curr.pop()
                    used[n] = False

        backtrack([])

        return out
