# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue1 = deque([root])
        queue2 = deque()
        ans = []

        while queue1 or queue2:
            lvl = []
            for i in range(len(queue1)):  # 1
                node = queue1.pop()  # 3
                lvl.append(node.val)  # [3]
                if node.left:  # 9
                    queue2.append(node.left)  # [9]
                if node.right:
                    queue2.append(node.right)  # [9, 20]
            if lvl:
                ans.append(lvl)  # [[3]]

            lvl = []
            for i in range(len(queue2)):  # 2
                node = queue2.pop()  # 20, 9
                lvl.append(node.val)  # [20, 9]
                if node.right:
                    queue1.append(node.right)
                if node.left:
                    queue1.append(node.left)
            if lvl:
                ans.append(lvl)

        return ans