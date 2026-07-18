/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func hasPathSum(root *TreeNode, targetSum int) bool {
    var dfs func(node *TreeNode, sum int) bool

    dfs = func(node *TreeNode, sum int) bool {
        if node == nil {
            return false
        }

        if node.Left == nil && node.Right == nil {
            if sum + node.Val == targetSum {
                return true
            }
            return false
        }

        L := dfs(node.Left, sum + node.Val)
        R := dfs(node.Right, sum + node.Val)

        return L || R
    }

    return dfs(root, 0)
}