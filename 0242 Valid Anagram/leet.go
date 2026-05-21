func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    a := make(map[byte]int)
    b := make(map[byte]int)

    for i := range len(s) {
        if _, ok := a[s[i]]; ok == false {
            a[s[i]] = 1
        } else {
            a[s[i]] += 1
        }
        if _, ok := b[t[i]]; ok == false {
            b[t[i]] = 1
        } else {
            b[t[i]] += 1
        }
    }

    for k := range a {
        if a[byte(k)] != b[byte(k)] {
            return false
        }
    }

    return true
}