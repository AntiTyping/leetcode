func permute(nums []int) [][]int {
    out := [][]int{}
    used := make([]bool, len(nums))

    var backtrack func(curr []int)

    backtrack = func (curr []int) {
        if len(curr) == len(nums) {
            cp := make([]int, len(curr))
            copy(cp, curr)
            out = append(out, cp)
            return
        }
        // O(n)
        for n := 0; n < len(nums); n++ {
            if used[n] {
                continue
            }
            used[n] = true
            curr = append(curr, nums[n])
            backtrack(curr)
            curr = curr[:len(curr)-1]
            used[n] = false
        }
    }

    backtrack([]int{})

    return out
}