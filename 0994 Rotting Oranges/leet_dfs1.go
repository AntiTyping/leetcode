const (
    empty = iota
    fresh
    rotten
)

type point struct {
    r, c int
}

var dirs = [4]point{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}

func orangesRotting(grid [][]int) int {
    rows, cols := len(grid), len(grid[0])

    isRotten := func(p point) bool {
        return grid[p.r][p.c] == rotten
    }

    isFresh := func(p point) bool {
        return grid[p.r][p.c] == fresh
    }

    infect := func(p point) {
        grid[p.r][p.c] = rotten
    }

    neighbours := func(p point) []point {
        ns := []point{}

        for _, d := range dirs {
            nr, nc := p.r + d.r, p.c + d.c
            if 0 <= nr && nr < rows && 0 <= nc && nc < cols {
                ns = append(ns, point{nr, nc})
            }
        }
        return ns
    }


    rotten := []point{}
    fresh := []point{}

    for r := range rows {
        for c := range cols {
            p := point{r, c}

            if isFresh(p) == true {
                fresh = append(fresh, p)
            }
            if isRotten(p) == true {
                rotten = append(rotten, p)
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
            for _, b := range neighbours(a) {
                if isFresh(b) {
                    infected++
                    infect(b)
                    if infected == len(fresh) {
                        return days
                    }
                    q = append(q, b)
                }
            }
        }
        days++
    }

    return -1
}