func orangesRotting(grid [][]int) int {
    rows := len(grid)
    cols := len(grid[0])

    isRotten := func(r, c int) bool {
        return grid[r][c] == 2
    }

    isFresh := func(r, c int) bool {
        return grid[r][c] == 1
    }

    infect := func(r, c int) {
        grid[r][c] = 2
    }

    neighbours := func(r, c int) [][]int {
        ns := [][]int{}
        dirs := [][]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}

        for _, d := range dirs {
            nr, nc := r + d[0], c + d[1]
            if 0 <= nr && nr < rows && 0 <= nc && nc < cols {
                ns = append(ns, []int{nr, nc})
            }
        }
        return ns
    }


    rotten := [][]int{}
    fresh := [][]int{}

    for r := range rows {
        for c := range cols {
            if isFresh(r, c) == true {
                fresh = append(fresh, []int{r, c})
            }
            if isRotten(r, c) == true {
                rotten = append(rotten, []int{r, c})
            }
        }
    }

    if len(fresh) == 0 {
        return 0
    }

    days := 1
    infected := 0

    q := rotten

    for len(q) > 0 {
        level := len(q)
        for range level {
            a := q[0]
            q = q[1:]
            for _, b := range neighbours(a[0], a[1]) {
                if isFresh(b[0], b[1]) {
                    infected++
                    infect(b[0], b[1])
                    if infected == len(fresh) {
                        return days
                    }
                    q = append(q, []int{b[0], b[1]})
                }
            }
        }
        days++
    }

    return -1
}