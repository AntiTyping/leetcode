package main

func LongestPalindrome(s string) int {
	return longestPalindrome(s)
}

func longestPalindrome(s string) int {
	h := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		h[s[i]]++
	}
	n := 0
	for _, v := range h {
		if v%2 == 1 {
			n = 1
			break
		}
	}

	for _, v := range h {
		if v%2 == 0 {
			n += v
		} else {
			n += v - 1
		}
	}

	return n
}

func main() {
	print(longestPalindrome("abccccdd"))
}
