# n log n + n
func containsDuplicate(nums []int) bool {
    sort.Ints(nums)
    for i := range nums[:len(nums)-1] {
        if nums[i] == nums[i+1] {
            return true
        }
    }
    return false
}