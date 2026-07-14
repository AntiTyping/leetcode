# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        mind = float('inf')

        def dfs(root, d):
            nonlocal mind
            if not root:
                return
            if not root.left and not root.right:
                mind = min(mind, d)
            else:
                dfs(root.left, d + 1)
                dfs(root.right, d + 1)

        dfs(root, 1)

        return mind if mind < float('inf') else 0

# >>> dis.dis(minDepth)
#   6           0 LOAD_GLOBAL              0 (float)
#               2 LOAD_CONST               1 ('inf')
#               4 CALL_FUNCTION            1
#               6 LOAD_DEREF               1 (self)
#               8 STORE_ATTR               1 (mind)
#
#   7          10 LOAD_CLOSURE             0 (dfs)
#              12 LOAD_CLOSURE             1 (self)
#              14 BUILD_TUPLE              2
#              16 LOAD_CONST               2 (<code object dfs at 0x107c2c870, file "<stdin>", line 7>)
#              18 LOAD_CONST               3 ('minDepth.<locals>.dfs')
#              20 MAKE_FUNCTION            8 (closure)
#              22 STORE_DEREF              0 (dfs)
#
#  15          24 LOAD_DEREF               0 (dfs)
#              26 LOAD_FAST                1 (root)
#              28 LOAD_CONST               4 (1)
#              30 CALL_FUNCTION            2
#              32 POP_TOP
#
#  16          34 LOAD_DEREF               1 (self)
#              36 LOAD_ATTR                1 (mind)
#              38 LOAD_GLOBAL              0 (float)
#              40 LOAD_CONST               1 ('inf')
#              42 CALL_FUNCTION            1
#              44 COMPARE_OP               0 (<)
#              46 POP_JUMP_IF_FALSE       54
#              48 LOAD_DEREF               1 (self)
#              50 LOAD_ATTR                1 (mind)
#              52 RETURN_VALUE
#         >>   54 LOAD_CONST               5 (0)
#              56 RETURN_VALUE
#
# Disassembly of <code object dfs at 0x107c2c870, file "<stdin>", line 7>:
#   8           0 LOAD_FAST                0 (root)
#               2 POP_JUMP_IF_TRUE         8
#
#   9           4 LOAD_CONST               0 (None)
#               6 RETURN_VALUE
#
#  10     >>    8 LOAD_FAST                0 (root)
#              10 LOAD_ATTR                0 (left)
#              12 POP_JUMP_IF_TRUE        36
#              14 LOAD_FAST                0 (root)
#              16 LOAD_ATTR                1 (right)
#              18 POP_JUMP_IF_TRUE        36
#
#  11          20 LOAD_GLOBAL              2 (min)
#              22 LOAD_DEREF               1 (self)
#              24 LOAD_ATTR                3 (mind)
#              26 LOAD_FAST                1 (d)
#              28 CALL_FUNCTION            2
#              30 LOAD_DEREF               1 (self)
#              32 STORE_ATTR               3 (mind)
#              34 JUMP_FORWARD            32 (to 68)
#
#  13     >>   36 LOAD_DEREF               0 (dfs)
#              38 LOAD_FAST                0 (root)
#              40 LOAD_ATTR                0 (left)
#              42 LOAD_FAST                1 (d)
#              44 LOAD_CONST               1 (1)
#              46 BINARY_ADD
#              48 CALL_FUNCTION            2
#              50 POP_TOP
#
#  14          52 LOAD_DEREF               0 (dfs)
#              54 LOAD_FAST                0 (root)
#              56 LOAD_ATTR                1 (right)
#              58 LOAD_FAST                1 (d)
#              60 LOAD_CONST               1 (1)
#              62 BINARY_ADD
#              64 CALL_FUNCTION            2
#              66 POP_TOP
#         >>   68 LOAD_CONST               0 (None)
#              70 RETURN_VALUE