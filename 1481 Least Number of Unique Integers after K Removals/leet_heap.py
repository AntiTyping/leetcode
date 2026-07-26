class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int

        """
        c = Counter(arr)

        heap = []
        for num,count in c.items():
            heap.append([count, num])

        heapify(heap)
        for _ in range(k):
            a = heappop(heap)
            if a[0] == 1:
                del c[a[1]]
            else:
                c[a[1]] -= 1
                a[0] -= 1
                heappush(heap, a)

        return len(c)
