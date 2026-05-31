class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        out = []

        def backtrack(curr, i, m, sum):
            if sum == target:
                out.append(curr[:])
                return
            elif sum > target:
                return
            else:
                for n in range(m, len(candidates)):
                    curr.append(candidates[n])
                    backtrack(curr, i+1, n, sum+candidates[n])
                    curr.pop()

        backtrack([], 0, 0, 0)

        return out