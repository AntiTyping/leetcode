func findLonely(nums []int) []int {
    freq := make(map[int]int)

    for _, num := range nums {
        freq[num]++
    }

    out := []int{}

    for _, num := range nums {
        if freq[num] == 1 && freq[num-1] == 0 && freq[num+1] == 0 {
            out = append(out, num)
        }
    }
    return out
}