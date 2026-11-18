/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */

func connect(root *Node) *Node {
    if root == nil {
        return root
    }
	q := []*Node{}

    q = append(q, root)

    for len(q) > 0 {
        level := len(q)

        for i := range (level - 1) {
            q[i].Next = q[i+1]
        }

        for range level {
            n := q[0]
            q[0] = nil
            q = q[1:]

            if n.Left != nil {
                q = append(q, n.Left)
            }
            if n.Right != nil {
                q = append(q, n.Right)
            }
        }
    }

    return root
}