func validPath(n int, edges [][]int, source int, destination int) bool {
    graph := make(map[int][]int)

    for _, e := range edges {
        u, v := e[0], e[1]

        graph[u] = append(graph[u], v)
        graph[v] = append(graph[v], u)
    }

    stack := []int{source}
    visited := make(map[int]struct{})
    visited[source] = struct{}{}

    for len(stack) > 0 {
        node := stack[0]
        stack = stack[1:]

        if node == destination {
            return true
        }

        for _, e := range graph[node] {
            if _, ok := visited[e]; !ok {
                visited[e] = struct{}{}
                stack = append(stack, e)
            }
        }
    }

    return false
}