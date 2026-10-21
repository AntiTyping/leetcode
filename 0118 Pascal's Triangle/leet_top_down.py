class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        @cache
        def dp(i):
            if i == 0:
                return [[1]]

            triangle = dp(i - 1)
            last_row = triangle[-1]
            ans = [1]
            for i in range(len(last_row) - 1):
                ans.append(last_row[i] + last_row[i + 1])
            ans.append(1)

            triangle.append(ans)
            return triangle

        return dp(numRows - 1)