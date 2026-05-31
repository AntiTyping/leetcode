func permute(nums []int) [][]int {
    out := [][]int{}

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
            // O(n)
            if slices.Contains(curr, nums[n]) {
                continue
            }
            curr = append(curr, nums[n])
            backtrack(curr)
            curr = curr[:len(curr)-1]
        }

    }

    backtrack([]int{})

    return out
}