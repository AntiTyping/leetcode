/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
    ans := 0

    var dfs func(node *TreeNode, d int)

    dfs = func(node *TreeNode, d int) {
        if node == nil {
            return
        }

        ans = slices.Max([]int{ans, d})

        dfs(node.Left, d + 1)
        dfs(node.Right, d + 1)
    }

    dfs(root, 1)

    return ans
}