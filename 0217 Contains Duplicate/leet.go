# n
func containsDuplicate(nums []int) bool {
    s := make(map[int]struct{})
    for i := range nums {
        x := nums[i]
        if _, ok := s[x]; ok == true {
            return true
        } else {
            s[x] = struct{}{}
        }
    }
    return false
}