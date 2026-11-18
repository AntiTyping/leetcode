func shortestPathBinaryMatrix(grid [][]int) int {
    if grid[0][0] == 1 {
        return -1
    }

    n := len(grid)
    neighbours := func(r, c int) [][]int {
        ns := [][]int{}
        dirs := [][]int{{-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}}
        for _, d := range dirs {
            dr, dc := d[0], d[1]
            nr, nc := r + dr, c + dc
            if 0 <= nr && nr < n && 0 <= nc && nc < n {
                ns = append(ns, []int{nr, nc})
            }
        }
        return ns
    }
    isOpen := func(r, c int) bool {
        return grid[r][c] == 0
    }
    q := [][]int{[]int{0, 0, 1}}
    visited := make(map[[2]int]struct{})
    visited[[2]int{0, 0}] = struct{}{}

    for len(q) > 0 {
        curr := q[0]
        q[0] = []int{}
        q = q[1:]
        r, c, l := curr[0], curr[1], curr[2]
        if r == n - 1 && c == n - 1 {
            return l
        }
        for _, ng := range neighbours(r, c) {
            ngr, ngc := ng[0], ng[1]
            if _, ok := visited[[2]int{ngr, ngc}]; !ok && isOpen(ngr, ngc) {
                visited[[2]int{ngr, ngc}] = struct{}{}
                q = append(q, []int{ngr, ngc, l+1})
            }
        }
    }

    return -1
}