# @param {Integer} mass
# @param {Integer[]} asteroids
# @return {Boolean}
def asteroids_destroyed(mass, asteroids)
    asteroids.sort!
    asteroids.each do |a|
        if mass >= a
            mass += a
        else
            return false
        end
    end
    return true
end