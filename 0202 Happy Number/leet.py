class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True

        return False

    def sumOfSquares(self, n):
        a = 0
        while n > 0:
            a = a + (n % 10) * (n % 10)
            n = n // 10
        return a

