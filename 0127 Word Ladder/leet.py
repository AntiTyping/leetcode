class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        def valid(n):
            return True

        dist = defaultdict(int)

        # O(l)
        def distance(w1, w2):
            if (w1, w2) in dist:
                return dist[(w1, w2)]
            d = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    d += 1
            dist[(w2, w1)] = d
            return d

        buckets = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                w1 = list(w)
                w1[i] = "*"
                buckets[tuple(w1)].append(w)

        # O(w*l)
        def find_neighbours(w):
            n = []
            for i in range(len(w)):
                w1 = list(w)
                w1[i] = "*"
                n.extend(buckets[tuple(w1)])

            return n

        neighbours = defaultdict(list)
        # O(w*w*l)
        for w in wordList:
            neighbours[w] = find_neighbours(w)
        neighbours[beginWord] = find_neighbours(beginWord)

        queue = deque()
        seen = set()

        queue.append((beginWord, 1))  # hit,0
        seen.add(beginWord)  # hit

        while queue:  # hit
            word, steps = queue.popleft()  # hit, 0

            if word == endWord:  # F
                return steps

            for n in neighbours[word]:
                if valid(n) and n not in seen:
                    seen.add(n)
                    queue.append((n, steps + 1))

        return 0

