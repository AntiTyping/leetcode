class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a = []

        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                a.append(nums1[i])
                i += 1
            else:
                a.append(nums2[j])
                j += 1

        while i < len(nums1):
            a.append(nums1[i])
            i += 1
        while j < len(nums2):
            a.append(nums2[j])
            j += 1

        # print(a)

        if len(a) % 2 == 0:
            mid = len(a) // 2
            return (float(a[mid - 1]) + a[mid]) / 2
        else:
            mid = len(a) // 2
            return a[mid]


