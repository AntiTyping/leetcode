/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func goodNodes(root *TreeNode) int {
    var dfs func(node *TreeNode, max int)

    ans := 0

    dfs = func(node *TreeNode, max int) {
        if node == nil {
            return
        }

        if node.Val >= max {
            ans += 1
        }

        max = slices.Max([]int{max, node.Val})

        dfs(node.Left, max)
        dfs(node.Right, max)

    }

    dfs(root, math.MinInt)

    return ans
}