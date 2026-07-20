class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #  [[1,1,0],
        #   [1,1,0],
        #   [0,0,1]]
        self.ans = 0

        self.seen = set()

        def dfs(start):
            stack = [start]
            while stack:
                node = stack.pop()
                self.seen.add(node)
                for i in range(len(isConnected[node])):
                    if isConnected[node][i] == 1 and i not in self.seen:
                        stack.append(i)

        for i in range(len(isConnected)):
            if i not in self.seen:
                self.ans += 1
            dfs(i)


        return self.ans

