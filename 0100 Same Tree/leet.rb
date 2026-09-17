# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initializewrite the plan
(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} p
# @param {TreeNode} q
# @return {Boolean}
def is_same_tree(p, q)
    if !p || !q
        p == q
    else
        p.val == q.val && is_same_tree(p.left, q.left) && is_same_tree(p.right, q.right)
    end
end