class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # n
        s = set(nums1)

        i = []
        for n in nums2:
            if n in s:
                i.append(n)
                s.remove(n)

        return i

