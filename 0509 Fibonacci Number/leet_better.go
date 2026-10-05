func fib(n int) int {
	a, b := 0, 1
	for range n {
		a, b = b, a+b
	}
	if n < 0 {
		return n
	}
	return a
}