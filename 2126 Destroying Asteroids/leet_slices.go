func asteroidsDestroyed(mass int, asteroids []int) bool {
    slices.Sort(asteroids)
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