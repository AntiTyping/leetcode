class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ans = []
        digits = []

        def bt():
            if len(digits) == n:
                ans.append(int("".join([str(d) for d in digits])))
                return

            for i in range(10):
                if abs(digits[-1] - i) == k:
                    digits.append(i)
                    bt()
                    digits.pop()

        for i in range(1, 10):
            digits.append(i)
            bt()
            digits.pop()

        return ans
