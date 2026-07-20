class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #  [[1,1,0],
        #   [1,1,0],
        #   [0,0,1]]
        self.ans = 0

        self.colors = [-1] * len(isConnected)
        self.seen = [0] * len(isConnected)

        def dfs(node, color):
            if self.colors[node] == -1:
                self.colors[node] = color
            self.seen[node] = 1
            for i in range(len(isConnected[node])):
                if isConnected[node][i] == 1 and self.seen[i] == 0:
                    dfs(i, color)

        for i in range(len(isConnected)):
            dfs(i, i)


        return len(set(self.colors))

