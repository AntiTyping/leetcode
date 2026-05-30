class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []

        def backtrack(curr, l, i):
            if l == k:
                ans.append(curr[:])
            else:
                for i in range(i, n+1):
                    curr.append(i)
                    backtrack(curr, l+1, i+1)
                    curr.pop()

        backtrack([], 0, 1)

        return list(ans)