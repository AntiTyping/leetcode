func isAlphaNum(b byte) bool {
    return (b >= 'a' && b <= 'z') || (b >= '0' && b <= '9')
}

func isPalindrome(s string) bool {

    left := 0
    right := len(s) - 1

    s1 := strings.ToLower(s)

    for left < right {
        for left < right && !isAlphaNum(s1[left])  {
            left += 1
        }
        for right > left && !isAlphaNum(s1[right]) {
            right -= 1
        }
        if left > right {
            return true
        }
        if s1[left] != s1[right] {
            return false
        }
        left += 1
        right -= 1
    }

    return true
}