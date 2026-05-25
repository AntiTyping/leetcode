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

        # n?
        return list(s1 & s2)