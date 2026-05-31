class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        out = []

        def backtrack(curr, i, m):
            if sum(curr) == target:
                out.append(curr[:])
                return
            elif sum(curr) > target:
                return
            else:
                for n in range(m, len(candidates)):
                    curr.append(candidates[n])
                    backtrack(curr, i+1, n)
                    curr.pop()

        backtrack([], 0, 0)

        return out