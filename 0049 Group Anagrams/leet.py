class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        h = {}
        for s in strs:
            ss = tuple(sorted(s))
            if ss in h:
                h[ss].append(s)
            else:
                h[ss] = [s]
        return h.values()
