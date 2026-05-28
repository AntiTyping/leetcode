func isStrobogrammatic(num string) bool {
    numbers := map[string]string{ "0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
    left, right := 0, len(num)-1
    for left <= right {
        if string(num[left]) == "" || string(num[left]) != numbers[string(num[right])] {
            return false
        }
        left++
        right--
    }
    return true
}