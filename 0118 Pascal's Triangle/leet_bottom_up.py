class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        ans.append([1])
        # O(n)
        for i in range(1, numRows):
            a = [1]
            dd = ans[-1]
            # O(n)
            for i in range(1, len(dd)):
                a.append(dd[i-1]+dd[i])
            a.append(1)
            ans.append(a)
        return ans
