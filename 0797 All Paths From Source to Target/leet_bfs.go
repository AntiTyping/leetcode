import "slices"

func allPathsSourceTarget(graph [][]int) [][]int {
    n := len(graph)
    q := [][]int{{0}}
    paths := [][]int{}

    for len(q) > 0 {
        path := q[0]
        q = q[1:]
        a := path[len(path) - 1]
        if a == n - 1 {
            paths = append(paths, slices.Clone(path))
        }
        for _, b := range graph[a] {
            q = append(q, slices.Clone(append(path, b)))
        }
    }

    return paths
}