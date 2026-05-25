class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # n
        s1 = set(nums1)
        # n
        s2 = set(nums2)

        i = []
        if len(s1) > len(s2):
            for s in s1:
                if s in s2:
                    i.append(s)
        else:
            for s in s2:
                if s in s1:
                    i.append(s)
        return i
