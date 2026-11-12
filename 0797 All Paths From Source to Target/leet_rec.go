
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
    current := []int{0}

    var dfs func(i int)

    dfs = func(node int) {
        if node == n - 1 {
            ans = append(ans, slices.Clone(current))
        }
        for _, e := range g[node] {
            current = append(current, e)
            dfs(e)
            current = current[:len(current)-1]
        }
    }

    dfs(0)

    return ans
}