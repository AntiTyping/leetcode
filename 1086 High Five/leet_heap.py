class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """

        heaps = defaultdict(list)

        for i in range(len(items)):
            heaps[items[i][0]].append(-items[i][1])
        for k in heaps:
            heapq.heapify(heaps[k])
        ans = []
        for k in heaps:
            ss = []
            for i in range(5):
                ss.append(heapq.heappop(heaps[k]))
            ans.append([k, -sum(ss) // 5])

        return ans