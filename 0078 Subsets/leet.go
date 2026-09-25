func subsets(nums []int) [][]int {
    ans := make([][]int,0 , 1<<len(nums))
    curr := make([]int, 0, len(nums))

    var bt func (start int)

    bt = func (start int) {
        ans = append(ans, slices.Clone(curr))

        for n := start; n < len(nums); n++ {
            curr = append(curr, nums[n])
            bt(n+1)
            curr = curr[0:len(curr)-1]
        }
    }

    bt(0)

    return ans
}