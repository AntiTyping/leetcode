func partitionArray(nums []int, k int) int {
    slices.Sort(nums)
    n := 1
    first := nums[0]
    for i := 1; i < len(nums); i++ {
        if nums[i] > first + k {
            n++
            first = nums[i]
        }
    }
    return n
}