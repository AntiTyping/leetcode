type point struct {
    r, c int
}
type entry struct {
    p point
    l int
}
func shortestPathBinaryMatrix(grid [][]int) int {
    if grid[0][0] == 1 {
        return -1
    }

    n := len(grid)
    neighbours := func(p point) []point {
        ns := []point{}
        dirs := [][]int{{-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}}
        for _, d := range dirs {
            dr, dc := d[0], d[1]
            np := point{p.r + dr, p.c + dc}
            if 0 <= np.r && np.r < n && 0 <= np.c && np.c < n {
                ns = append(ns, np)
            }
        }
        return ns
    }
    isOpen := func(p point) bool {
        return grid[p.r][p.c] == 0
    }
    q := []entry{entry{point{0, 0}, 1}}
    visited := make(map[point]struct{})
    visited[point{0, 0}] = struct{}{}

    for len(q) > 0 {
        curr := q[0]
        q[0] = entry{}
        q = q[1:]
        p, l := curr.p, curr.l
        if p.r == n - 1 && p.c == n - 1 {
            return l
        }
        for _, ng := range neighbours(p) {
            if _, ok := visited[ng]; !ok && isOpen(ng) {
                visited[ng] = struct{}{}
                q = append(q, entry{ng, l + 1})
            }
        }
    }

    return -1
}