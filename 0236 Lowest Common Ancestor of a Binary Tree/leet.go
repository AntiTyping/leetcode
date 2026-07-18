/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    var dfs func(*TreeNode) *TreeNode

    dfs = func(node *TreeNode) *TreeNode {
        if node == nil {
            return nil
        }

        if node == p || node == q {
            return node
        }

        L := dfs(node.Left)
        R := dfs(node.Right)

        if L != nil && R != nil {
            return node
        }

        if L != nil {
            return L
        }

        return R
    }
    return dfs(root)
}