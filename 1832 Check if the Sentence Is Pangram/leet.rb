# @param {String} sentence
# @return {Boolean}
def check_if_pangram(sentence)
    letters = Array.new(26, 0)

    sentence.each_char do |c|
        letters[c.ord - 'a'.ord] += 1
    end

    letters.each do |f|
        if f == 0
            return false
        end
    end

    return true
end