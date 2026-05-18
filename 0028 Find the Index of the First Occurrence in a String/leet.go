func strStr(haystack string, needle string) int {
    if len(haystack) < len(needle) {
        return -1
    }

    n := len(needle)
    left := 0
    for left <= len(haystack) - n {
        if strings.Compare(haystack[left:left+n], needle) == 0 {
            return left
        }
        left += 1
    }
    return -1
}