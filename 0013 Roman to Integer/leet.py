class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "II": 2,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        left = 0
        right = 0


        number = 0

        while left < len(s):
            if s[left:left+2] in roman:
                number += roman[s[left:left+2]]
                left += 2
            else:
                number += roman[s[left:left+1]]
                left += 1

        return number


