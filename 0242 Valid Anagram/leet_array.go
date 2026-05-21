func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    var a [26]int

    for i := range len(s) {
        a[s[i] - 'a'] += 1
        a[t[i] - 'a'] -= 1
    }

    for i := range len(a) {
        if a[i] != 0 {
            return false
        }
    }

    return true
}