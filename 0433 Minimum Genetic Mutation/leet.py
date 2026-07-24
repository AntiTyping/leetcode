class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        a = ['A', 'C', 'G', 'T']

        self.seen = set()

        start = startGene

        # 8*4 = 32
        queue = deque()
        seen = set()

        queue.append((startGene, 0))
        seen.add(startGene)

        while queue:
            node, steps = queue.popleft()
            if node == endGene:
                return steps
            for i in range(8):
                for j in range(4):
                    new_node = list(node)
                    new_node[i] = a[j]
                    new_node = "".join(new_node)
                    if new_node in bank and new_node not in seen:
                        seen.add(new_node)
                        queue.append((new_node, steps + 1))

        return -1
