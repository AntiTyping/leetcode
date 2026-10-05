func fib(n int) int {
    if n == 0 {
        return 0
    }
    a := make([]int, n + 1)

    a[1] = 1
    for i := 2; i < n + 1; i++ {
        a[i] = a[i - 1] + a[i - 2]
    }

    return a[n]
}