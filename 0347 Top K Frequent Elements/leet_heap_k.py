class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        counter = defaultdict(int)

        # O(n)
        for n in nums:
            counter[n] += 1

        # O(n)
        heap = []

        for num, count in counter.items():
            heappush(heap, (count, num))
            if len(heap) > k:
                heappop(heap)

        # O(k)
        return [h[1] for h in heap]

