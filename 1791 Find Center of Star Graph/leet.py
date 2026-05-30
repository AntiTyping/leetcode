class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        return Counter([x for sub in edges for x in sub]).most_common()[0][0]
