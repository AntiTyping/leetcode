class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1 = defaultdict(int)

        for n in nums1:
            d1[n] += 1

        o = []
        for n in nums2:
            if n in d1:
                o.append(n)
                if d1[n] > 1:
                    d1[n] -= 1
                else:
                    del d1[n]
        return o
