/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func deepestLeavesSum(root *TreeNode) int {
    ans := 0
    queue := []*TreeNode{}

    queue = append(queue, root)

    for len(queue) > 0 {
        ans = 0
        levelLen := len(queue)
        for i := 0; i < levelLen; i++ {
            node := queue[0]
            queue = queue[1:]
            ans += node.Val

            if node.Left != nil {
                queue = append(queue, node.Left)
            }
            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }
    }

    return ans
}