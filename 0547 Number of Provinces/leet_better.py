class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #  [[1,1,0],
        #   [1,1,0],
        #   [0,0,1]]
        self.ans = 0

        self.seen = [0] * len(isConnected)

        def dfs(node, color):
            self.seen[node] = 1
            for i in range(len(isConnected[node])):
                if isConnected[node][i] == 1 and self.seen[i] == 0:
                    dfs(i, color)

        for i in range(len(isConnected)):
            if self.seen[i] == 0:
                self.ans += 1
            dfs(i, i)


        return self.ans

