class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if "0000" in deadends:
            return -1
        queue = deque()
        seen = set(deadends)

        queue.append(("0000", 0))
        seen.add("0000")

        while queue:
            node, steps = queue.popleft()
            if node == target:
                return steps
            for i in range(4):
                l = list(node)
                c = int(l[i])
                if c < 9:
                    c += 1
                    l[i] = str(c)
                    next_node = "".join(l)
                    if next_node not in seen:
                        seen.add(next_node)
                        queue.append((next_node, steps+1))
            for i in range(4):
                l = list(node)
                c = int(l[i])
                if c == 0:
                    c = 10
                if c > 0:
                    c -= 1
                    l[i] = str(c)
                    next_node = "".join(l)
                    if next_node not in seen:
                        seen.add(next_node)
                        queue.append((next_node, steps+1))

        return -1

