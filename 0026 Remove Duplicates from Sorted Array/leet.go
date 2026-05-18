func removeDuplicates(nums []int) int {
    left := 0
    right := 0

    for right < len(nums) {
        if nums[left] == nums[right] {
            right += 1
        } else {
            left += 1
            nums[left] = nums[right]
            right += 1
        }
    }
    return left + 1
}