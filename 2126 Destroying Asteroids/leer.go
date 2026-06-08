func asteroidsDestroyed(mass int, asteroids []int) bool {
    sort.Ints(asteroids)
    m := mass
    for i := range asteroids {
        if m >= asteroids[i] {
            m += asteroids[i]
        } else {
            return false
        }
    }
    return true
}