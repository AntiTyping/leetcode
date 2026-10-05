func fib(n int) int {

    memo := make(map[int]int)

    var f func(int) int

    f = func(n int) int {
        if n <= 1 {
            return n
        }

        if k, ok := memo[n]; ok == true {
            return k
        }

        memo[n] = f(n - 1) + f(n - 2)

        return memo[n]
    }

    return f(n)
}