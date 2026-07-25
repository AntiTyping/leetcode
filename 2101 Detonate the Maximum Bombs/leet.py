class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """

        def distance(a, b):
            dx = b[0] - a[0]
            dy = b[1] - a[1]
            return math.sqrt(dx ** 2 + dy ** 2)

        def valid(j):
            return True

        def find_neighbours(j):  # 1
            n = []
            a = bombs[j]  # 6,1,4
            for i in range(len(bombs)):  # 0
                b = bombs[i]  # 2,1,3
                if i != j and distance(a, b) <= a[2]:
                    n.append(i)
            return n

        neighbours = defaultdict(list)
        for i in range(len(bombs)):
            neighbours[i] = find_neighbours(i)

        ans = 0
        for i in range(len(bombs)):
            exploded = 1
            queue = deque()
            seen = set()

            queue.append(i)
            seen.add(i)

            while queue:
                j = queue.popleft()
                for n in neighbours[j]:
                    if valid(n) and n not in seen:
                        exploded += 1
                        seen.add(n)
                        queue.append(n)

            ans = max(ans, exploded)

        return ans
