func mergeAlternately(word1 string, word2 string) string {
    ch1 := make(chan byte, len(word1))
    ch2 := make(chan byte, len(word2))

    go func() {
        for _, b := range []byte(word1) {
            ch1 <- b
        }
        close(ch1)
    }()
    go func() {
        for _, b := range []byte(word2) {
            ch2 <- b
        }
        close(ch2)
    }()
    out := make([]byte, len(word1)+len(word2))
    c1 := ch1
    var c2 chan byte
    i := 0
    for i < len(word1) + len(word2) {
        select {
            case b, ok := <- c1:
                    if !ok {
                        ch1 = nil
                        c1 = nil
                    } else {
                        out[i] = b
                        i++
                    }
                    if ch2 != nil {
                        c1 = nil
                        c2 = ch2
                    }
            case b, ok := <- c2:
                    if !ok {
                        ch2 = nil
                        c2 = nil
                    } else {
                        out[i] = b
                        i++
                    }
                    if ch1 != nil {
                        c1 = ch1
                        c2 = nil
                    }
        }
    }
    return string(out)
}