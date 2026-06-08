function asteroidsDestroyed(mass: number, asteroids: number[]): boolean {
    asteroids.sort((a,  b) => a-b)
    let m = mass
    for(const a of asteroids) {
        if (m >= a) {
            m += a
        } else {
            return false
        }
    }
    return true
};