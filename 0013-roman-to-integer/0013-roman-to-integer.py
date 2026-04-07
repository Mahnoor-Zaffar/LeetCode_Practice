class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        } # storing values as dictionary
        
        total = 0
        for i in range(len(s)): #iterates one by one
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]: 
                total -= roman_map[s[i]] #substract if we get a special case
            else:
                total += roman_map[s[i]] # value greate then next add
        return total
        