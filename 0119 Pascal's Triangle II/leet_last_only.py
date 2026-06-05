class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        first = [1]
        for i in range(1, rowIndex+1):
            last = first
            a = [1]
            for j in range(len(last)-1):
                a.append(last[j]+last[j+1])
            a.append(1)
            first = a
        return first

