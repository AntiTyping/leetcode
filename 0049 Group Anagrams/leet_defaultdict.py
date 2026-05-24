class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        h = defaultdict(list)
        for s in strs:
            ss = [0] * 26
            for ch in s:
                ss[ord(ch)-ord("a")] = ss[ord(ch)-ord("a")] + 1
            ss = tuple(ss)

            h[ss].append(s)
        return h.values()
