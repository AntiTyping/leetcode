# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """

        def dfs(node, parent):
            if not node:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        def neighbours(self):
            return [self.left, self.right, self.parent]

        TreeNode.neighbours = neighbours

        self.seen = set()
        self.ans = []

        def bfs(node, distance):
            if not node:
                return
            self.seen.add(node)
            if distance > k:
                return
            if distance == k:
                self.ans.append(node.val)
            else:
                for n in node.neighbours():
                    if n not in self.seen:
                        bfs(n, distance + 1)

        a = bfs(target, 0)

        return self.ans
