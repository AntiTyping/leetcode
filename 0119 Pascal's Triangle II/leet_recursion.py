class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def dp(n):
            if n == 0:
                return [1]
            elif n == 1:
                return [1,1]
            else:
                parent = dp(n-1)
                a = [1]
                for i in range(len(parent)-1):
                    a.append(parent[i]+parent[i+1])
                a.append(1)
                return a
        return dp(rowIndex)