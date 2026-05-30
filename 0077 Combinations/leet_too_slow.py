class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = set()

        def backtrack(curr, l):
            if l == k:
                if len(set(curr[:])) == len(curr):
                    ans.add(tuple(sorted(curr[:])))
            else:
                for i in range(1, n+1):
                    curr.append(i)
                    backtrack(curr, l+1)
                    curr.pop()

        backtrack([], 0)

        return list(ans)