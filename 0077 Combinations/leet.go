func combine(n int, k int) [][]int {
    out := [][]int{}

    var backtrack func(curr []int, l int)

    backtrack = func(curr []int, l int) {
        if len(curr) == k {
            // O(k)
            cp := make([]int, len(curr))
            copy(cp, curr)
            out = append(out, cp)
        }
        // O(n)
        for i := l; i <= n; i++ {
            curr = append(curr, i)
            backtrack(curr, i + 1)
            curr = curr[:len(curr)-1]
        }
    }
    // b [], 0
    //

    backtrack([]int{}, 1)

    return out
}