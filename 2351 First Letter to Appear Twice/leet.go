func repeatedCharacter(s string) byte {
    seen := make(map[byte]struct{})
    for i, _ := range s {
        c := s[i]
        if _, ok := seen[c]; ok {
            return c
        } else {
            seen[c] = struct{}{}
        }
    }
    return 0
}