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
        inverted = [(-v, k) for k, v in counter.items()]

        # O(n)
        heapify(inverted)

        # O(k)
        return [heappop(inverted)[1] for i in range(k)]

