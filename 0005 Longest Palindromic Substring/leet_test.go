package main

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestLongestPalindrome(t *testing.T) {
	assert.Equal(t, 7, longestPalindrome("abccccdd"))
}

func BenchmarkLongestPalindrome(b *testing.B) {
	for i := 0; i < b.N; i++ {
		longestPalindrome("abccccdd")
	}
}

func ExampleLongestPalindrome() {
	fmt.Println(longestPalindrome("abccccdd"))
	// Output: 7
}

func FuzzLongestPalindrome(f *testing.F) {
	f.Add(7, "abccccdd")
	f.Fuzz(func(t *testing.T, i int, s string) {
		if i != longestPalindrome(s) {
			t.Errorf("Expected %d, got %d", i, longestPalindrome(s))
		}
	})
}
