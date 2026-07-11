package main

func checkIfPangram(sentence string) bool {
    var letters [26]int

    for _, l := range sentence {
        letters[l-'a']++
    }

    for l := range len(letters) {
        if letters[l] == 0 {
            return false
        }
    }

    return true
}

func main() {
    print(checkIfPangram("leetcode"))
}