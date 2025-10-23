func mergeAlternately(word1 string, word2 string) string {
    ch := make(chan byte)

    go func() {
        i, j := 0, 0
        for i < len(word1) || j < len(word2) {
            if i < len(word1) {
                ch <- word1[i]
                i++
            }
            if j < len(word2) {
                ch <- word2[j]
                j++
            }
        }
        close(ch)
    }()
    out := make([]byte, len(word1)+len(word2))
    i := 0
    for b := range ch {
        out[i] = b
    }
    return string(out)
}