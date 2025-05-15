func longestPalindrome(s string) string {
    p := ""

    for i, _ := range s {
        j, k := i, i
        for j > -1 && k < len(s) && s[j] == s[k] {
            new_p := s[j:k+1]
            if len(new_p) > len(p) {
                p = new_p
            }
            j--
            k++
        }
        j, k = i, i + 1
        for j > -1 && k < len(s) && s[j] == s[k] {
            new_p := s[j:k+1]
            if len(new_p) > len(p) {
                p = new_p
            }
            j--
            k++
        }
    }
    return p

}