
import "slices"
func allPathsSourceTarget(graph [][]int) [][]int {
    n := len(graph)
    g := make(map[int][]int)

    for i := 0; i < len(graph); i++ {
        for _, u := range graph[i] {
            g[i] = append(g[i], u)
        }
    }

    var ans [][]int

    stack := [][]int{{0}}

    for len(stack) > 0 {
        path := stack[0]
        stack = stack[1:]
        node := path[len(path) - 1]
        if node == n - 1 {
            ans = append(ans, slices.Clone(path))
        }
        for _, e := range g[node] {
            stack = append(stack, append(append([]int{}, path...), e))
        }
    }

    return ans
}