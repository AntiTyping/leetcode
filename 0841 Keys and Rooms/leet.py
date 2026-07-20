class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        self.seen = [0] * len(rooms)

        def dfs(room):
            self.seen[room] = 1
            keys = rooms[room]
            for key in keys:
                if self.seen[key] == 0:
                    dfs(key)

        dfs(0)

        return sum(self.seen) == len(rooms)