class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        def dp(n):
            if n == 1:
                ans.append([1])
            elif n == 2:
                dp(n-1)
                ans.append([1, 1])
            else:
                dp(n-1)
                a = [1]
                last = ans[-1]
                for i in range(len(last)-1):
                    a.append(last[i]+last[i+1])
                a.append(1)
                ans.append(a)
        out = dp(numRows)
        return ans
