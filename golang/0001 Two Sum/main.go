// Instead of checking every pair (slow), we store each number in a hash map as we go. For each new number, we ask: "Have I already seen the complement that would add up to the target?" If yes, we found our answer instantly!

func twoSum(nums []int, target int) []int {
    var seen = make(map[int]int)

    for i, num := range nums {
        complement := target - num
        if j, found := seen[complement]; found {
            return []int{j, i}
        }
        seen[num] = i
    }
    return nil
}