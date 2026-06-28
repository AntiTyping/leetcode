
import "sort"
func missingNumber(nums []int) int {
    sort.Ints(nums)

    if nums[0] != 0 {
        return 0
    }

    for i := range nums {
        if i > 0 {
            if nums[i-1] + 1 != nums[i] {
                return nums[i] -1
            }
        }
    }

    return len(nums)
}
