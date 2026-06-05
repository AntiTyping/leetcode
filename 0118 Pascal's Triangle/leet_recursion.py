class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        def dp(n):
            if n == 1:
                return [[1]]
            # elif n == 2:
            #     return dp(n-1) + [[1, 1]]
            else:
                parent = dp(n - 1)
                last = parent[-1]
                a = [1]
                for i in range(len(last) - 1):
                    a.append(last[i] + last[i + 1])
                a.append(1)
                return parent + [a]

        return dp(numRows)